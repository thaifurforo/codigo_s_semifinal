"""Module that contains the Transaction View Set.
"""

from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from virtual_bank.models import Transaction
from virtual_bank.serializers import TransactionSerializer

# Create your views here.


class TransactionViewSet(viewsets.ModelViewSet):
    """This class creates a ModelViewSet for the Transaction serializer.

    It allows the following http methods to be used on the requests for this view:
    get, post, delete, head, options.
    Therefore, it's not possible to update an transaction after it was already created.
    It's only possible to delete it and create another, if needed.

    The queryset determinates that the Transaction objects will be shown first by
    date, then by debit_account, then by credit_account, and finally by
    transaction_type.

    The serializer class used for this view is the TransactionSerializer.

    There are set some filters for this ViewSet:
    The data can be ordered by date or amount.
    The data can be searched by debit_account, credit_account or transaction_type.
    The data can be filtered by selecting the transaction_type, by selecting the
    date (exact, greater than or equal, less than or equal), by selecting the amount
    (exact, greater than or equal, less than or equal), by selecting a specific
    debit_account and/or by selecting a specific credit_account.

    The authentication for this ViewSet is BasicAuthentication, which means that the
    authentication is made through an user an password combination.
    The permission class is IsAuthenticated, which means that it alows access to
    any authenticated user, and denies access to any unauthenticated user.
    """

    http_method_names = ['get', 'post', 'delete', 'head', 'options']

    queryset = Transaction.objects.all().order_by(
        'date', 'debit_account', 'credit_account', 'transaction_type'
    )

    serializer_class = TransactionSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    ordering_fields = ['date', 'amount']
    search_fields = ['debit_account', 'credit_account', 'transaction_type']
    filterset_fields = {
        'transaction_type': ['exact'],
        'date': ['gte', 'lte', 'exact'],
        'amount': ['gte', 'lte', 'exact'],
        'debit_account': ['exact'],
        'credit_account': ['exact'],
    }

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        """Overrides the get_serializer method for this ViewSet, which returns
        the serializer instance that should be used for validating and deserializing
        input, and for serializing output.
        Turns possible to make multiple POST requests at the same time, using an
        array of objects in the JSON file.
        """

        if 'data' in kwargs:
            data = kwargs['data']

            if isinstance(data, list):
                kwargs['many'] = True

        return super().get_serializer(*args, **kwargs)
