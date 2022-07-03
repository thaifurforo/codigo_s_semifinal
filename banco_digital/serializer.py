from rest_framework import serializers
from banco_digital.models import Cliente, Conta
from banco_digital.validators import *

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
  class Meta():
    model = Cliente
    fields = ['url', 'id', 'tipo', 'cpf_cnpj', 'nome_razao_social', 'endereco', 'telefone', 'email', 'data_nascimento']

  def validate(self, data):
    """Valida se os dados preenchidos em cada campo estão de acordo com os formatos adequados"""

    if not cpf_cnpj_tamanho_valido(data['cpf_cnpj'], data['tipo']):
      if data['tipo'] == 'PF':
        raise serializers.ValidationError({'cpf_cnpj':'O CPF deve ter 11 dígitos'})
      else:
        raise serializers.ValidationError({'cpf_cnpj':'O CNPJ deve ter 14 dígitos'})

    if not cpf_cnpj_digito_verificador_valido(data['cpf_cnpj'], data['tipo']):
      raise serializers.ValidationError({'cpf_cnpj':'CPF/CNPJ inválido'})
    
    if not data_nascimento_se_pf(data['data_nascimento'], data['tipo']):
      raise serializers.ValidationError({'data_nascimento':'Obrigatório preencher Data de Nascimento para Pessoas Físicas'})

    if not data_nascimento_se_pj(data['data_nascimento'], data['tipo']):
      raise serializers.ValidationError({'data_nascimento':'Pessoa Jurídica não deve ter Data de Nascimento'})

    return data

class ContaSerializer(serializers.HyperlinkedModelSerializer):
  class Meta():
    model = Conta
    fields = ['url', 'numero_completo_conta', 'cliente', 'data_abertura', 'conta_ativa', 'data_encerramento']

  def validate(self, data):
    """Valida se os dados preenchidos em cada campo estão de acordo com os formatos adequados"""

    if not conta_inativa_se_data_encerramento(data['data_encerramento'], data['conta_ativa']):
      raise serializers.ValidationError({'conta_ativa': 'Somente contas inativas podem ter data de encerramento'})

    if not data_encerramento_se_conta_inativa(data['data_encerramento'], data['conta_ativa']):
      raise serializers.ValidationError({'data_encerramento': 'Inserir a data de encerramento da conta inativa'})

    if not data_encerramento_maior_data_abertura(data['data_encerramento'], data['data_abertura']):
      raise serializers.ValidationError({'data_encerramento': 'A data de encerramento da conta deve ser maior que a data de abertura'})

    # if not conta_inativa_saldo_zerado(data['saldo'], data['data_encerramento']):
    #   raise serializers.ValidationError({'saldo': 'A conta só poderá ser encerrada se houver saldo'})

    return data


    
 
    
      
