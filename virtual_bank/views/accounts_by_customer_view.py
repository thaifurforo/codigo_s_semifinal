from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from virtual_bank.models.account_model import Account
from virtual_bank.serializers import AccountsByCustomerSerializer


class AccountsByCustomerView(generics.ListAPIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # Listing all accounts from the selected customer
    def get_queryset(self):
        queryset = Account.objects.filter(
            customer_id=self.kwargs['pk']).order_by('-active_account', 'opening_date')
        return queryset

    serializer_class = AccountsByCustomerSerializer
