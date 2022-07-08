from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from virtual_bank.models import Account
from virtual_bank.serializers import AccountSerializer

# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
  queryset = Account.objects.all()
  serializer_class = AccountSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]
