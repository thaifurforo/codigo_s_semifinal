from rest_framework import serializers
from banco_digital.models import Cliente, Conta
from banco_digital.validators import *

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
  class Meta():
    model = Cliente
    fields = ['url', 'id', 'tipo', 'cpf_cnpj', 'nome_razao_social', 'endereco', 'telefone', 'email']

  def validate(self, data):
    """Valida se os dados preenchidos em cada campo estão de acordo com os formatos adequados"""

    if not cpf_cnpj_tamanho_valido(data['cpf_cnpj'], data['tipo']):
      if data['tipo'] == 'PF':
        raise serializers.ValidationError({'cpf_cnpj':'O CPF deve ter 11 dígitos'})
      else:
        raise serializers.ValidationError({'cpf_cnpj':'O CNPJ deve ter 14 dígitos'})

    # if not telefone_valido(data['telefone']):
    #   raise serializers.ValidationError({'telefone':'Formato do telefone inválido'})

    if not cpf_cnpj_digito_verificador_valido(data['cpf_cnpj'], data['tipo']):
      raise serializers.ValidationError({'cpf_cnpj':'CPF/CNPJ inválido'})

    return data

class ContaSerializer(serializers.HyperlinkedModelSerializer):
  class Meta():
    model = Conta
    fields = ['url', 'numero_completo_conta', 'cliente', 'conta_ativa', 'saldo']
    
 
    
      
