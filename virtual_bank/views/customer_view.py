from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from virtual_bank.models import Customer
from virtual_bank.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.all().order_by('id')

    serializer_class = CustomerSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    ordering_fields = ['name']
    search_fields = ['name', 'document_number']
    filterset_fields = {'customer_type': ['exact'], 'birthdate': ['gte', 'lte']}

    def get_serializer(self, *args, **kwargs):
        if 'data' in kwargs:
            data = kwargs['data']

            if isinstance(data, list):
                kwargs['many'] = True

        return super().get_serializer(*args, **kwargs)

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
