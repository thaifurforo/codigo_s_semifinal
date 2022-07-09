from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from virtual_bank.models import Transaction
from virtual_bank.serializers import TransactionSerializer

# Create your views here.


class TransactionViewSet(viewsets.ModelViewSet):

    queryset = Transaction.objects.all().order_by(
        'date', 'debit_account', 'credit_account', 'transaction_type')

    serializer_class = TransactionSerializer

    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ['date', 'amount']
    search_fields = ['debit_account', 'credit_account', 'transaction_type']
    filterset_fields = {'transaction_type': ['exact'], 'date': [
        'gte', 'lte', 'exact'], 'amount': [
        'gte', 'lte', 'exact'], 'debit_account': ['exact'], 'credit_account': ['exact']}

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
