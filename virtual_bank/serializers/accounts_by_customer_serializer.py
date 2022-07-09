from rest_framework import serializers
from virtual_bank.models.account_model import Account


class AccountsByCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
