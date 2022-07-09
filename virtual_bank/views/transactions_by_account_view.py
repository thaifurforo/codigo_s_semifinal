from django.db.models import Q
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from virtual_bank.models.transaction_model import Transaction
from virtual_bank.serializers.transactions_by_account_serializer import TransactionsByAccountSerializer


class TransactionsByAccountView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # Listing all accounts from the selected customer

    def get_queryset(self):
        queryset = Transaction.objects.filter(
            Q(credit_account_id=self.kwargs['pk']) | Q(debit_account_id=self.kwargs['pk']))
        return queryset
    serializer_class = TransactionsByAccountSerializer