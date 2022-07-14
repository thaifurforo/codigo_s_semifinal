from rest_framework import serializers

from virtual_bank.models.balance_model import Balance


class BalanceSerializer(serializers.ModelSerializer):
    """This class creates a ModelSerializer for the Balance model."""

    class Meta:
        """Sets the Balance as the model used on this serializer, and establishes
        the fields that are shown in the serialized result"""

        model = Balance
        fields = ('balance',)
