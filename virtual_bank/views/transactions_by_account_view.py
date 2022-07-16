"""Module that contains the Transactions by Account List API View.
"""

from django.db.models import Q
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from virtual_bank.models import Transaction
from virtual_bank.serializers import TransactionsByAccountSerializer


class TransactionsByAccountView(generics.ListAPIView):
    """This class creates a ListAPIView for the Transaction by Account serializer,
    which filters all the Transaction objects for each Account.

    It allows only the GET http methods to be used on the requests for this view.

    The serializer class used for this view is the TransactionsByAccountSerializer.

    The authentication for this ViewSet is BasicAuthentication, which means that the
    authentication is made through an user an password combination.
    The permission class is IsAuthenticated, which means that it alows access to
    any authenticated user, and denies access to any unauthenticated user.
    """

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = TransactionsByAccountSerializer

    def get_queryset(self):
        """This overrides the method get_queryset for this Class, returning a
        queryset with the Transaction objects filtered by the debit_account and
        credit_account from the selected account on the ListAPIView.

        Also determinates that the Transaction objects will be shown first by date,
        then by transaction_type, and finally by amount.
        """

        queryset = Transaction.objects.filter(
            Q(credit_account_id=self.kwargs['pk'])
            | Q(debit_account_id=self.kwargs['pk'])
        ).order_by('date', 'transaction_type', 'amount')

        return queryset
