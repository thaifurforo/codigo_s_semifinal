from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from virtual_bank.models import Transaction
from virtual_bank.serializers.account_serializer import AccountSerializer
from virtual_bank.validators import *


class TransactionSerializer(serializers.ModelSerializer):
    """This class creates a ModelSerializer for the Transaction model."""

    class Meta():
        """Sets the Transaction as the model used on this serializer and establishes
        the fields that are shown in the serialized result."""
        model = Transaction
        fields = ('url', 'id', 'transaction_type', 'date',
                  'amount', 'debit_account', 'credit_account')

    def validate(self, data):
        """Validates the request data according to validators logics"""

        if not transaction_decimals_validate(data['amount']):
            raise serializers.ValidationError(
                {'amount': 'O valor da transação deve ter até duas casas decimais'})

        if not debit_transactions_validation(data['transaction_type'], data['debit_account']):
            raise serializers.ValidationError(
                {'debit_account': 'É necessário informar uma conta para crédito do valor neste tipo de transação'})

        if not credit_transactions_validation(data['transaction_type'], data['credit_account']):
            raise serializers.ValidationError(
                {'credit_account': 'É necessário informar uma conta para crédito do valor neste tipo de transação'})

        if not not_debit_transactions_validation(data['transaction_type'], data['debit_account']):
            raise serializers.ValidationError(
                {'debit_account': 'Inválido informar uma conta de débito neste tipo de transação'})

        if not not_credit_transactions_validation(data['transaction_type'], data['credit_account']):
            raise serializers.ValidationError(
                {'credit_account': 'Inválido informar uma conta de crédito neste tipo de transação'})

        return data
