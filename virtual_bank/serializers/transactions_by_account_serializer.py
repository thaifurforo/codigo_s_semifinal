from rest_framework import serializers
from virtual_bank.models.transaction_model import Transaction


class TransactionsByAccountSerializer(serializers.ModelSerializer):
    # Returns the description for the transaction type, instead of the initials
    transaction_type = serializers.SerializerMethodField()

    def get_transaction_type(self, obj):
        return obj.get_transaction_type_display()

    class Meta:
        model = Transaction
        fields = '__all__'
