from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from virtual_bank.models import Account
from virtual_bank.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):

    queryset = Account.objects.all().order_by(
        '-active_account', 'opening_date', 'closure_date', 'account_number')

    serializer_class = AccountSerializer

    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ['opening_date',
                       'closure_date', 'customer', 'customer_id']
    search_fields = ['account_number']
    filterset_fields = {'active_account': ['exact'], 'opening_date': [
        'gte', 'lte', 'exact'],  'closure_date': ['gte', 'lte', 'exact'], 'customer': ['exact']}

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
