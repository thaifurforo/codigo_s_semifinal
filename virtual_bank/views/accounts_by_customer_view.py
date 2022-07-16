"""Module that contains the Accounts by Customer List API View.
"""

from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from virtual_bank.models import Account
from virtual_bank.serializers import AccountsByCustomerSerializer


class AccountsByCustomerView(generics.ListAPIView):
    """This class creates a ListAPIView for the Account by Customer serializer,
    which filters all the Accounts objects for each Customer.

    It allows only the GET http methods to be used on the requests for this view.

    The serializer class used for this view is the AccountsByCustomerSerializer.

    The authentication for this ViewSet is BasicAuthentication, which means that the
    authentication is made through an user an password combination.
    The permission class is IsAuthenticated, which means that it alows access to
    any authenticated user, and denies access to any unauthenticated user.
    """

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = AccountsByCustomerSerializer

    def get_queryset(self):
        """This overrides the method get_queryset for this Class, returning a
        queryset with the Account objects filtered by the customer_id from the
        selected customer on the ListAPIView.

        Also determinates that the Account objects will be shown first by active_accounts,
        then by opening_date, then by closure_date, and finally by account_number.
        """

        queryset = Account.objects.filter(customer_id=self.kwargs['pk']).order_by(
            '-active_account', 'opening_date', 'closure_date', 'account_number'
        )

        return queryset
