from rest_framework import serializers
from virtual_bank.models import Transaction
from virtual_bank.validators import *

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
  class Meta():
    model = Transaction
    fields = '__all__'

  def validate(self, data):
    """Valida se os dados preenchidos em cada campo estão de acordo com os formatos adequados"""
    if not transaction_decimals_validate(data['amount']):
      raise serializers.ValidationError({'amount':'O parâmetro "amount" deve ser um integer ou uma string com somente números'})
