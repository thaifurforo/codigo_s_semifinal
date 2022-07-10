from rest_framework import serializers
from virtual_bank.models.transaction_model import Transaction


class TransactionsByAccountSerializer(serializers.ModelSerializer):
    # Returns the description for the transaction type, instead of the initials
    class Meta:
        model = Transaction
        fields = ('url', 'id', 'transaction_type', 'date',
                  'amount', 'debit_account', 'credit_account')
