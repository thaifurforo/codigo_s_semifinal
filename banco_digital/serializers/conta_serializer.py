from rest_framework import serializers
from banco_digital.models import Conta
from banco_digital.validators import *

class ContaSerializer(serializers.HyperlinkedModelSerializer):
  class Meta():
    model = Conta
    fields = ['url', 'numero_completo_conta', 'cliente', 'data_abertura', 'conta_ativa', 'data_encerramento']

  def validate(self, data):
    """Valida se os dados preenchidos em cada campo estão de acordo com os formatos adequados"""

    if not inactive_account_if_closure_date_validate(data['data_encerramento'], data['conta_ativa']):
      raise serializers.ValidationError({'conta_ativa': 'Somente contas inativas podem ter data de encerramento'})

    if not closure_date_if_inactive_account_validate(data['data_encerramento'], data['conta_ativa']):
      raise serializers.ValidationError({'data_encerramento': 'Inserir a data de encerramento da conta inativa'})

    if not closure_date_greater_then_opening_date_validate(data['data_encerramento'], data['data_abertura']):
      raise serializers.ValidationError({'data_encerramento': 'A data de encerramento da conta deve ser maior que a data de abertura'})

    # if not conta_inativa_saldo_zerado(data['saldo'], data['data_encerramento']):
    #   raise serializers.ValidationError({'saldo': 'A conta só poderá ser encerrada se houver saldo'})

    return data


    
 
    
      
