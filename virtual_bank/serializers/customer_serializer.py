from rest_framework import serializers
from virtual_bank.models import Customer
from virtual_bank.validators import *

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
  class Meta():
    model = Customer
    fields = '__all__'

  def validate(self, data):
    """Valida se os dados preenchidos em cada campo estão de acordo com os formatos adequados"""

    if not document_number_numbers_only_validate(data['document_number']):
      raise serializers.ValidationError({'document_number':'O parâmetro "document_number" deve ser um integer ou uma string com somente números'})


    if data['tipo'] == 'PF':

      if not cpf_length_validate(data['document_number']):
        raise serializers.ValidationError({'document_number':'O CPF deve ter 11 dígitos'})

      if not cpf_check_digit_validate(data['document_number']):
        raise serializers.ValidationError({'document_number':'CPF inválido'})

      if not birth_date_if_pf_validate(data['data_nascimento']):
        raise serializers.ValidationError({'data_nascimento':'Obrigatório preencher Data de Nascimento para Pessoas Físicas'})

    
    if data['tipo'] == 'PJ':

      if not cnpj_length_validate(data['document_number']):
        raise serializers.ValidationError({'document_number':'O CNPJ deve ter 14 dígitos'})

      if not cnpj_check_digit_validate(data['document_number']):
        raise serializers.ValidationError({'document_number':'CNPJ inválido'})

      if not not_birth_date_if_pj_validate(data['data_nascimento']):
        raise serializers.ValidationError({'data_nascimento':'Pessoa Jurídica não deve ter Data de Nascimento'})

    return data