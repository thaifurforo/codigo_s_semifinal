from rest_framework import serializers
from virtual_bank.models import Transaction
from virtual_bank.validators import *


class TransactionSerializer(serializers.ModelSerializer):
    """This class creates a ModelSerializer for the Transaction model."""

    class Meta:
        """Sets the Transaction as the model used on this serializer and establishes
        the fields that are shown in the serialized result."""

        model = Transaction
        fields = (
            'url',
            'id',
            'transaction_type',
            'date',
            'amount',
            'debit_account',
            'credit_account',
        )

    def validate_amount(self, value):
        """Validates the amount field creation (transactions can't be updated)"""

        if not transaction_decimals_validate(value):
            raise serializers.ValidationError(
                'O valor da transação deve ter até duas casas decimais'
            )

        return value

    def validate(self, data):
        """Validates multiple fields creation (transactions can't be updated)"""

        if self.context['request'].method == "POST":

            if not debit_transactions_validation(
                data['transaction_type'], data['debit_account']
            ):
                raise serializers.ValidationError(
                    {
                        'debit_account': 'É necessário informar uma conta para crédito do valor neste tipo de transação'
                    }
                )

            if not credit_transactions_validation(
                data['transaction_type'], data['credit_account']
            ):
                raise serializers.ValidationError(
                    {
                        'credit_account': 'É necessário informar uma conta para crédito do valor neste tipo de transação'
                    }
                )

            if not not_debit_transactions_validation(
                data['transaction_type'], data['debit_account']
            ):
                raise serializers.ValidationError(
                    {
                        'debit_account': 'Inválido informar uma conta de débito neste tipo de transação'
                    }
                )

            if not not_credit_transactions_validation(
                data['transaction_type'], data['credit_account']
            ):
                raise serializers.ValidationError(
                    {
                        'credit_account': 'Inválido informar uma conta de crédito neste tipo de transação'
                    }
                )

            if data['debit_account'] != None:

                debit_account_opening_date = data['debit_account'].opening_date
                if not transaction_date_more_recent_than_account_opening_date(
                    data['date'], debit_account_opening_date
                ):
                    raise serializers.ValidationError(
                        {
                            'date': f'Data da transação deve ser igual ou posterior à data de abertura da conta debitada: {debit_account_opening_date}'
                        }
                    )

                debit_account_active = data['debit_account'].active_account
                if not transaction_in_active_account(debit_account_active):
                    raise serializers.ValidationError(
                        {
                            'credit_account': f'Não é possível realizar débito em conta já encerrada'
                        }
                    )

            if data['credit_account'] != None:

                credit_account_opening_date = data['credit_account'].opening_date
                if not transaction_date_more_recent_than_account_opening_date(
                    data['date'], credit_account_opening_date
                ):
                    raise serializers.ValidationError(
                        {
                            'date': f'Data da transação deve ser igual ou posterior à data de abertura da conta creditada: {credit_account_opening_date}'
                        }
                    )

                credit_account_active = data['credit_account'].active_account
                if not transaction_in_active_account(credit_account_active):
                    raise serializers.ValidationError(
                        {
                            'credit_account': f'Não é possível realizar crédito em conta já encerrada'
                        }
                    )

        return data
