from rest_framework import serializers
from virtual_bank.models.address_model import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta():
        model = Address
        fields = ('city', 'district', 'neighborhood', 'street')
