from rest_framework import serializers

from virtual_bank.models.balance_model import Balance


class BalanceSerializer(serializers.ModelSerializer):

    class Meta():
        model = Balance
        fields = ('balance', )
