from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from virtual_bank.models import Account
from virtual_bank.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):

    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']

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

    def get_serializer(self, *args, **kwargs):
        if 'data' in kwargs:
            data = kwargs['data']

            if isinstance(data, list):
                kwargs['many'] = True

        return super().get_serializer(*args, **kwargs)

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
