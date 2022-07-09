from rest_framework import serializers
from virtual_bank.models import Customer
from virtual_bank.models.address_model import Address
from virtual_bank.serializers.address_serializer import AddressSerializer
from virtual_bank.validators import *


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
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

    class Meta():
        model = Customer
        fields = ('url', 'client_type', 'document_number', 'name', 'phone_number', 'email', 'birthdate',
                  'zip_code', 'city', 'district', 'neighborhood', 'street', 'door_number', 'complement')
        depth = 1

    def validate(self, data):
        """Valida se os dados preenchidos em cada campo estão de acordo com os formatos adequados"""

        if not document_number_numbers_only_validate(data['document_number']):
            raise serializers.ValidationError(
                {'document_number': 'O parâmetro "document_number" deve ser um integer ou uma string com somente números'})

        if data['client_type'] == 'PF':

            if not cpf_length_validate(data['document_number']):
                raise serializers.ValidationError(
                    {'document_number': 'O CPF deve ter 11 dígitos'})

            if not cpf_check_digit_validate(data['document_number']):
                raise serializers.ValidationError(
                    {'document_number': 'CPF inválido'})

            if not birthdate_if_pf_validate(data['birthdate']):
                raise serializers.ValidationError(
                    {'birthdate': 'Obrigatório preencher Data de Nascimento para Pessoas Físicas'})

        if data['client_type'] == 'PJ':

            if not cnpj_length_validate(data['document_number']):
                raise serializers.ValidationError(
                    {'document_number': 'O CNPJ deve ter 14 dígitos'})

            if not cnpj_check_digit_validate(data['document_number']):
                raise serializers.ValidationError(
                    {'document_number': 'CNPJ inválido'})

            if not not_birthdate_if_pj_validate(data['birthdate']):
                raise serializers.ValidationError(
                    {'birthdate': 'Pessoa Jurídica não deve ter Data de Nascimento'})

        return data
