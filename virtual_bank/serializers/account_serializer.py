from rest_framework import serializers
from virtual_bank.models import Account
from virtual_bank.models.balance_model import Balance
from virtual_bank.serializers.balance_serializer import BalanceSerializer
from virtual_bank.validators import *


class AccountSerializer(serializers.ModelSerializer):
    #balance = BalanceSerializer(read_only=True, many=False).data
    balance = serializers.ReadOnlyField(source='balance.balance')

    customer_document = serializers.CharField(
        source='customer.name', read_only=True)

    customer_name = serializers.CharField(
        source='customer.name', read_only=True)

    class Meta():
        model = Account
        fields = ['url', 'account_number', 'customer', 'customer_document', 'customer_name',
                  'opening_date', 'active_account', 'closure_date', 'balance']

    def validate(self, data):
        """Validates the request data by format and other specifications"""

        # balance = Balance.objects.filter(account_id=self)

        if not inactive_account_if_closure_date_validate(data['closure_date'], data['active_account']):
            raise serializers.ValidationError(
                {'active_account': 'Somente contas inativas podem ter data de encerramento'})

        # if not inactive_account_if_balance_zero(data['active_account'], balance):
        #     raise serializers.ValidationError(
        #         {'active_account': f'Só é possível encerrar a conta se o saldo atual for igual a 0 - saldo atual: {balance}'})

        if not closure_date_if_inactive_account_validate(data['closure_date'], data['active_account']):
            raise serializers.ValidationError(
                {'closure_date': 'Inserir a data de encerramento da conta inativa'})

        if not closure_date_greater_than_opening_date_validate(data['closure_date'], data['opening_date']):
            raise serializers.ValidationError(
                {'closure_date': 'A data de encerramento da conta deve ser maior que a data de abertura'})

        # if not closure_date_bigger_than_last_transaction_date(data['closure_date'], data['account_number']):
        #     raise serializers.ValidationError(
        #         {'closure_date': 'A data de encerramento da conta deve ser maior que a data da última transação realizada na conta'})

        return data
