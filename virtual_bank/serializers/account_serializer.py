from rest_framework import serializers
from virtual_bank.models import Account
from virtual_bank.validators import *


class AccountSerializer(serializers.ModelSerializer):
    """This class creates a ModelSerializer for the Account model.

    Imports the Balance object vinculated to the Account object and adds it's "balance"
    field as a balance field (read only) to be shown in the serialized result.

    Adds a customer_document field (read only) to be shown in the serialized result 
    according to the customer vinculated to the Account's document_number.

    Adds a customer_name field (read only) to be shown in the serialized result 
    according to the customer vinculated to the Account's name.
    """

    balance = serializers.ReadOnlyField(source='balance.balance')

    customer_document = serializers.CharField(
        source='customer.document_number', read_only=True)

    customer_name = serializers.CharField(
        source='customer.name', read_only=True)

    class Meta():
        """Sets the Account as the model used on this serializer, and establishes
        the fields that are shown in the serialized result"""
        model = Account
        fields = ['url', 'id', 'account_number', 'customer', 'customer_document', 'customer_name',
                  'opening_date', 'active_account', 'closure_date', 'balance']

    def validate_customer(self, value):
        """Raises an error message in case the client tries to set a customer
        field (update) for the account object after it's already created"""

        if self.instance and value != self.instance.customer:
            raise serializers.ValidationError(
                'Não é possível alterar o cliente vinculado à conta após a mesma ter sido criada')
        return value

    def validate(self, data):
        """Validates the request data according to validators logics"""

        if not inactive_account_if_closure_date_validate(data['closure_date'], data['active_account']):
            raise serializers.ValidationError(
                {'active_account': 'Somente contas inativas podem ter data de encerramento'})

        if not closure_date_if_inactive_account_validate(data['closure_date'], data['active_account']):
            raise serializers.ValidationError(
                {'closure_date': 'Inserir a data de encerramento da conta inativa'})

        if not closure_date_greater_than_opening_date_validate(data['closure_date'], data['opening_date']):
            raise serializers.ValidationError(
                {'closure_date': 'A data de encerramento da conta deve ser maior que a data de abertura'})

        return data
