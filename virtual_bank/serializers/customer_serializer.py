from rest_framework import serializers
from virtual_bank.models import Customer
from virtual_bank.models.address_model import Address
from virtual_bank.serializers.address_serializer import AddressSerializer
from virtual_bank.validators import *


class CustomerSerializer(serializers.ModelSerializer):
    """This class creates a ModelSerializer for the Customer model.

    Adds the following fields (read only) from the Address' objects, according to
    the zip_code field of the Customer model, to be shown in the serialized result:
    city, district, neighborhood and street.
    """

    city = serializers.SerializerMethodField()

    def get_city(self, obj):
        address_queryset = Address.objects.filter(zip_code=obj.zip_code)
        address_serializer = AddressSerializer(address_queryset, many=True)
        return address_serializer.data[0]['city']

    district = serializers.SerializerMethodField()

    def get_district(self, obj):
        address_queryset = Address.objects.filter(zip_code=obj.zip_code)
        address_serializer = AddressSerializer(address_queryset, many=True)
        return address_serializer.data[0]['district']

    neighborhood = serializers.SerializerMethodField()

    def get_neighborhood(self, obj):
        address_queryset = Address.objects.filter(zip_code=obj.zip_code)
        address_serializer = AddressSerializer(address_queryset, many=True)
        return address_serializer.data[0]['neighborhood']

    street = serializers.SerializerMethodField()

    def get_street(self, obj):
        address_queryset = Address.objects.filter(zip_code=obj.zip_code)
        address_serializer = AddressSerializer(address_queryset, many=True)
        return address_serializer.data[0]['street']

    class Meta:
        """Sets the Customer as the model used on this serializer and establishes
        the fields that are shown in the serialized result."""

        model = Customer
        fields = (
            'url',
            'id',
            'customer_type',
            'document_number',
            'name',
            'phone_number',
            'email',
            'birthdate',
            'zip_code',
            'city',
            'district',
            'neighborhood',
            'street',
            'door_number',
            'complement',
        )

    def validate_document_number(self, value):
        """Validates the document_number field creation and updates"""

        if not document_number_numeric_validate(value):
            raise serializers.ValidationError('Este campo deve ter somente números')

        return value

    def validate_zip_code(self, value):
        """Validates the zip_code field creation and updates"""

        if not zip_code_format_valid(value):
            raise serializers.ValidationError('Formato de CEP inválido')

        if not zip_code_found(value):
            raise serializers.ValidationError('CEP não encontrado')

        return value

    def validate(self, data):
        """Validates multiple fields creation/update"""

        if 'customer_type' in data:
            customer_type = data['costumer_type']
        else:
            customer_type = self.instance.customer_type

        if customer_type == 'PF':

            if 'document_number' in data:

                if not cpf_length_validate(data['document_number']):
                    raise serializers.ValidationError(
                        {'document_number': 'O CPF deve ter 11 dígitos'}
                    )

                if not cpf_check_digit_validate(data['document_number']):
                    raise serializers.ValidationError(
                        {'document_number': 'CPF inválido'}
                    )

            if 'birthdate' in data:

                if not birthdate_not_null(data['birthdate']):
                    raise serializers.ValidationError(
                        {
                            'birthdate': 'Obrigatório preencher Data de Nascimento para Pessoas Físicas'
                        }
                    )

        if customer_type == 'PJ':

            if 'document_number' in data:

                if not cnpj_length_validate(data['document_number']):
                    raise serializers.ValidationError(
                        {'document_number': 'O CNPJ deve ter 14 dígitos'}
                    )

                if not cnpj_check_digit_validate(data['document_number']):
                    raise serializers.ValidationError(
                        {'document_number': 'CNPJ inválido'}
                    )

            if 'birthdate' in data:

                if birthdate_not_null(data['birthdate']):
                    raise serializers.ValidationError(
                        {'birthdate': 'Pessoa Jurídica não deve ter Data de Nascimento'}
                    )

        return data
