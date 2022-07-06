from rest_framework import serializers
from banco_digital.models import Cliente
from banco_digital.validators import *
from banco_digital.validators import not_birth_date_if_pj_validate

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
  class Meta():
    model = Cliente
    fields = ['url', 'id', 'tipo', 'cpf_cnpj', 'nome_razao_social', 'endereco', 'telefone', 'email', 'data_nascimento']

  def validate(self, data):
    """Valida se os dados preenchidos em cada campo estão de acordo com os formatos adequados"""

    if not cpf_cnpj_numbers_only_validate(data['cpf_cnpj']):
      raise serializers.ValidationError({'cpf_cnpj':'O parâmetro "cpf_cnpj" deve ser um integer ou uma string com somente números'})


    if data['tipo'] == 'PF':

      if not cpf_length_validate(data['cpf_cnpj']):
        raise serializers.ValidationError({'cpf_cnpj':'O CPF deve ter 11 dígitos'})

      if not cpf_check_digit_validate(data['cpf_cnpj']):
        raise serializers.ValidationError({'cpf_cnpj':'CPF inválido'})

      if not birth_date_if_pf_validate(data['data_nascimento']):
        raise serializers.ValidationError({'data_nascimento':'Obrigatório preencher Data de Nascimento para Pessoas Físicas'})

    
    if data['tipo'] == 'PJ':

      if not cnpj_length_validate(data['cpf_cnpj']):
        raise serializers.ValidationError({'cpf_cnpj':'O CNPJ deve ter 14 dígitos'})

      if not cnpj_check_digit_validate(data['cpf_cnpj']):
        raise serializers.ValidationError({'cpf_cnpj':'CNPJ inválido'})

      if not not_birth_date_if_pj_validate(data['data_nascimento']):
        raise serializers.ValidationError({'data_nascimento':'Pessoa Jurídica não deve ter Data de Nascimento'})

    return data