"""Module that contains the Account Model Serializer.
"""

from rest_framework import serializers
from virtual_bank.models import Account, Transaction
from virtual_bank.validators import (change_opening_date,
                                     activate_account_after_inactivated,
                                     closure_date_if_inactive_account_validate,
                                     inactive_account_if_balance_zero,
                                     inactive_account_if_closure_date_validate,
                                     closure_date_more_recent_than_last_transaction_date,
                                     closure_date_more_recent_than_opening_date_validate,
                                     change_customer)


class AccountSerializer(serializers.ModelSerializer):
    """This class creates a ModelSerializer for the Account model.

    Imports the Balance object vinculated to the Account object and adds it's "balance"
    field as a balance field (read only) to be shown in the serialized result.

    Adds a customer_document field (read only) to be shown in the serialized result
    according to the customer vinculated to the Account's document_number.

    Adds a customer_name field (read only) to be shown in the serialized result
    according to the customer vinculated to the Account's name.
    """

    balance = serializers.ReadOnlyField(source='balance.balance')

    customer_document = serializers.CharField(
        source='customer.document_number', read_only=True
    )

    customer_name = serializers.CharField(
        source='customer.name', read_only=True)

    class Meta:
        """Sets the Account as the model used on this serializer, and establishes
        the fields that are shown in the serialized result"""

        model = Account
        fields = [
            'url',
            'id',
            'account_number',
            'customer',
            'customer_document',
            'customer_name',
            'opening_date',
            'active_account',
            'closure_date',
            'balance',
        ]

    def validate_opening_date(self, value):
        """Validates the opening_date field creation and updates"""
        if self.instance:

            if change_opening_date(value, self.instance.opening_date):
                raise serializers.ValidationError(
                    'Não é possível alterar a data de abertura da conta '
                    'após a mesma ter sido criada'
                )

        return value

    def validate_active_account(self, value):
        """Validates the active_account field creation and updates"""
        if self.instance:

            if activate_account_after_inactivated(value, self.instance.active_account):
                raise serializers.ValidationError(
                    'Não é possível reativar a conta após a mesma ter sido encerrada'
                )

            if not inactive_account_if_balance_zero(
                value, self.instance.balance.balance
            ):
                raise serializers.ValidationError(
                    'Só é possível encerrar a conta se o saldo atual for igual a 0. '
                    f' Saldo atual: {self.instance.balance.balance}'
                )

        return value

    def validate_closure_date(self, value):
        """Validates the closure_data field creation and updates"""
        if self.instance:

            credit_transactions = (
                Transaction.objects.filter(credit_account=self.instance.id)
                .order_by('-date')
                .values_list('date')
            )
            if len(credit_transactions) == 0:
                last_credit_transaction_date = None
            else:
                last_credit_transaction_date = credit_transactions[0][0]

            debit_transactions = (
                Transaction.objects.filter(debit_account=self.instance.id)
                .order_by('-date')
                .values_list('date')
            )
            if len(debit_transactions) == 0:
                last_debit_transaction_date = None
            else:
                last_debit_transaction_date = debit_transactions[0][0]

            if not closure_date_more_recent_than_last_transaction_date(
                last_credit_transaction_date, last_debit_transaction_date, value
            ):
                raise serializers.ValidationError(
                    'A data de encerramento da conta deve ser maior ou igual à '
                    'data da última transação'
                )

            if not closure_date_more_recent_than_opening_date_validate(
                value, self.instance.opening_date
            ):
                raise serializers.ValidationError(
                    'A data de encerramento da conta deve ser maior que a data '
                    f'de abertura: {self.instance.opening_date}'
                )

        return value

    def validate_customer(self, value):
        """Validates the customer field creation and updates"""
        if self.instance:

            if change_customer(value, self.instance.customer):
                raise serializers.ValidationError(
                    'Não é possível alterar o cliente vinculado à conta após '
                    'a mesma ter sido criada'
                )

        return value

    def validate(self, attrs):
        """Validates multiple fields creation/update"""

        if self.context['request'].method == "POST":
            if not closure_date_more_recent_than_opening_date_validate(
                attrs['closure_date'], attrs['opening_date']
            ):
                raise serializers.ValidationError(
                    {
                        'closure_date': 'A data de encerramento da conta deve ser maior '
                        f'que a data de abertura: {attrs["opening_date"]}'
                    }
                )

        if 'closure_date' in attrs and 'active_account' in attrs:
            if not inactive_account_if_closure_date_validate(
                attrs['closure_date'], attrs['active_account']
            ):
                raise serializers.ValidationError(
                    {
                        'active_account:'
                        'Somente contas inativas podem ter data de encerramento'
                    }
                )

            if not closure_date_if_inactive_account_validate(
                attrs['closure_date'], attrs['active_account']
            ):
                raise serializers.ValidationError(
                    {'closure_date': 'Inserir a data de encerramento da conta inativa'}
                )

        elif 'closure_date' in attrs:
            raise serializers.ValidationError(
                {
                    'active_account': 'Somente contas inativas podem ter data de encerramento'
                }
            )

        elif 'active_account' in attrs:
            raise serializers.ValidationError(
                {'closure_date': 'Inserir a data de encerramento da conta inativa'}
            )

        return attrs
