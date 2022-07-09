from rest_framework import serializers
from virtual_bank.models.account_model import Account


class AccountsByCustomerSerializer(serializers.ModelSerializer):

    balance = serializers.ReadOnlyField(source='balance.balance')

    class Meta:
        model = Account
        fields = ('account_number', 'active_account',
                  'opening_date', 'closure_date', 'balance')
