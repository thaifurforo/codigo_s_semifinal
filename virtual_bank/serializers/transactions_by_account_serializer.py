from rest_framework import serializers
from virtual_bank.models.transaction_model import Transaction


class TransactionsByAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'
