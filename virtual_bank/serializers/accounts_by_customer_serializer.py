from rest_framework import serializers
from virtual_bank.models.account_model import Account


class AccountsByCustomerSerializer(serializers.ModelSerializer):
    """This class creates a ModelSerializer for the Account model to be used for a
    ListAPIView to show all accounts for a selected customer.

    Imports the Balance object vinculated to the Account object and adds it's "balance"
    field as a balance field (read only) to be shown in the serialized result.
    """

    balance = serializers.ReadOnlyField(source='balance.balance')

    class Meta:
        """Sets the Account as the model used on this serializer, and establishes
        the fields that are shown in the serialized result"""

        model = Account
        fields = ('url', 'id', 'account_number', 'active_account',
                  'opening_date', 'closure_date', 'balance')
