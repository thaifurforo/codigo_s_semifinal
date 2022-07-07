from rest_framework import serializers
from virtual_bank.models import Account
from virtual_bank.validators import *

class AccountSerializer(serializers.HyperlinkedModelSerializer):
  class Meta():
    model = Account
    fields = ['url', 'account_complete_number', 'customer', 'opening_date', 'active_account', 'closure_date']

  def validate(self, data):
    """Valida se os dados preenchidos em cada campo estão de acordo com os formatos adequados"""

    if not inactive_account_if_closure_date_validate(data['closure_date'], data['active_account']):
      raise serializers.ValidationError({'active_account': 'Somente contas inativas podem ter data de encerramento'})

    if not closure_date_if_inactive_account_validate(data['closure_date'], data['active_account']):
      raise serializers.ValidationError({'closure_date': 'Inserir a data de encerramento da conta inativa'})

    if not closure_date_greater_then_opening_date_validate(data['closure_date'], data['data_abertura']):
      raise serializers.ValidationError({'closure_date': 'A data de encerramento da conta deve ser maior que a data de abertura'})

    # if not conta_inativa_saldo_zerado(data['saldo'], data['closure_date']):
    #   raise serializers.ValidationError({'saldo': 'A conta só poderá ser encerrada se houver saldo'})

    return data


    
 
    
      
