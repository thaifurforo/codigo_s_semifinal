from rest_framework import serializers
from virtual_bank.models.transaction_model import Transaction


class TransactionsByAccountSerializer(serializers.ModelSerializer):
    """This class creates a ModelSerializer for the Transaction model to be used
    for a ListAPIView to show all transactions for a selected account.
    """

    class Meta:
        """Sets the Transaction as the model used on this serializer, and establishes
        the fields that are shown in the serialized result"""

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
