from rest_framework import serializers
from virtual_bank.models.address_model import Address


class AddressSerializer(serializers.ModelSerializer):
    """This class creates a ModelSerializer for the Address model."""

    class Meta:
        """Sets the Address as the model used on this serializer, and establishes
        the fields that are shown in the serialized result"""

        model = Address
        fields = ('city', 'district', 'neighborhood', 'street')
