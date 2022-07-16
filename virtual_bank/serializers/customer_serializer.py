"""Module that contains the Customer Model Serializer.
"""

from rest_framework import serializers
from virtual_bank.models import Customer, Address
from virtual_bank.serializers.address_serializer import AddressSerializer
from virtual_bank.validators import (document_number_numeric_validate,
                                     birthdate_not_null,
                                     cnpj_check_digit_validate,
                                     cnpj_length_validate,
                                     cpf_check_digit_validate,
                                     cpf_length_validate,
                                     zip_code_format_valid,
                                     zip_code_found)


class CustomerSerializer(serializers.ModelSerializer):
    """This class creates a ModelSerializer for the Customer model.

    Adds the following fields (read only) from the Address' objects, according to
    the zip_code field of the Customer model, to be shown in the serialized result:
    city, district, neighborhood and street.
    """

    city = serializers.SerializerMethodField()

    def get_city(self, obj):
        """Method to get the city field from the Address object with the same 
        zip_code from the Customer object

        Args:
            obj (Customer): Customer object

        Returns:
            city (str): Returns the string value of the city field on the Address
            object with the same zip_code from the Customer object (obj)
        """

        address_queryset = Address.objects.filter(zip_code=obj.zip_code)
        address_serializer = AddressSerializer(address_queryset, many=True)
        city = address_serializer.data[0]['city']
        return city

    district = serializers.SerializerMethodField()

    def get_district(self, obj):
        """Method to get the district field from the Address object with the same 
        zip_code from the Customer object

        Args:
            obj (Customer): Customer object

        Returns:
            district (str): Returns the string value of the district field on the Address
            object with the same zip_code from the Customer object (obj)
        """

        address_queryset = Address.objects.filter(zip_code=obj.zip_code)
        address_serializer = AddressSerializer(address_queryset, many=True)
        district = address_serializer.data[0]['district']
        return district

    neighborhood = serializers.SerializerMethodField()

    def get_neighborhood(self, obj):
        """Method to get the neighborhood field from the Address object with the
        same zip_code from the Customer object

        Args:
            obj (Customer): Customer object

        Returns:
            neighborhood (str): Returns the string value of the city field on the
            Address object with the same zip_code from the Customer object (obj)
        """

        address_queryset = Address.objects.filter(zip_code=obj.zip_code)
        address_serializer = AddressSerializer(address_queryset, many=True)
        neighborhood = address_serializer.data[0]['neighborhood']
        return neighborhood

    street = serializers.SerializerMethodField()

    def get_street(self, obj):
        """Method to get the street field from the Address object with the same 
        zip_code from the Customer object

        Args:
            obj (Customer): Customer object

        Returns:
            street (str): Returns the string value of the street field on the Address
            object with the same zip_code from the Customer object (obj)
        """

        address_queryset = Address.objects.filter(zip_code=obj.zip_code)
        address_serializer = AddressSerializer(address_queryset, many=True)
        street = address_serializer.data[0]['street']
        return street

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
            raise serializers.ValidationError(
                'Este campo deve ter somente números')

        return value

    def validate_zip_code(self, value):
        """Validates the zip_code field creation and updates"""

        if not zip_code_format_valid(value):
            raise serializers.ValidationError('Formato de CEP inválido')

        if not zip_code_found(value):
            raise serializers.ValidationError('CEP não encontrado')

        return value

    def validate(self, attrs):
        """Validates multiple fields creation/update"""

        if 'customer_type' in attrs:
            customer_type = attrs['customer_type']
        else:
            customer_type = self.instance.customer_type

        if customer_type == 'PF':

            if 'document_number' in attrs:

                if not cpf_length_validate(attrs['document_number']):
                    raise serializers.ValidationError(
                        {'document_number': 'O CPF deve ter 11 dígitos'}
                    )

                if not cpf_check_digit_validate(attrs['document_number']):
                    raise serializers.ValidationError(
                        {'document_number': 'CPF inválido'}
                    )

            if 'birthdate' in attrs:

                if not birthdate_not_null(attrs['birthdate']):
                    raise serializers.ValidationError(
                        {
                            'birthdate': 'Obrigatório preencher Data de Nascimento \
                                para Pessoas Físicas'
                        }
                    )

        if customer_type == 'PJ':

            if 'document_number' in attrs:

                if not cnpj_length_validate(attrs['document_number']):
                    raise serializers.ValidationError(
                        {'document_number': 'O CNPJ deve ter 14 dígitos'}
                    )

                if not cnpj_check_digit_validate(attrs['document_number']):
                    raise serializers.ValidationError(
                        {'document_number': 'CNPJ inválido'}
                    )

            if 'birthdate' in attrs:

                if birthdate_not_null(attrs['birthdate']):
                    raise serializers.ValidationError(
                        {'birthdate': 'Pessoa Jurídica não deve ter Data de Nascimento'}
                    )

        return attrs
