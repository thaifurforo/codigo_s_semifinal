"""Module that contains the Account View Set.
"""

from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from virtual_bank.models import Account
from virtual_bank.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    """This class creates a ModelViewSet for the Account serializer.

    It allows the following http methods to be used on the requests for this view:
    get, post, put, patch, head, options.
    Therefore, it's not possible to delete an account. It can only be turn active
    or inactive (when closed).

    The queryset determinates that the Account objects will be shown first by
    active_accounts, then by opening_date, then by closure_date, and finally by
    account_number.

    The serializer class used for this view is the AccountSerializer.

    There are set some filters for this ViewSet:
    The data can be ordered by opening_date, closure_date or customer.
    The data can be searched by account_number.
    The data can be filtered by selecting if the active_account is True or False,
    by selecting a opening_date (exact, greater than or equal, less than or equal),
    by selecting a closure_date (exact, greater than or equal, less than or equal),
    and/or by selecting a specific customer or multiple customers in a list or range.

    The authentication for this ViewSet is BasicAuthentication, which means that the
    authentication is made through an user an password combination.
    The permission class is IsAuthenticated, which means that it alows access to
    any authenticated user, and denies access to any unauthenticated user.
    """

    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']

    queryset = Account.objects.all().order_by(
        '-active_account', 'opening_date', 'closure_date', 'account_number'
    )

    serializer_class = AccountSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    ordering_fields = ['opening_date',
                       'closure_date', 'customer']
    search_fields = ['account_number']
    filterset_fields = {
        'active_account': ['exact'],
        'opening_date': ['gte', 'lte', 'exact'],
        'closure_date': ['gte', 'lte', 'exact'],
        'customer': ['exact', 'in'],
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
