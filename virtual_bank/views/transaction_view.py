from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from virtual_bank.models import Transaction
from virtual_bank.serializers import TransactionSerializer

# Create your views here.
class TransactionViewSet(viewsets.ModelViewSet):
  queryset = Transaction.objects.all()
  serializer_class = TransactionSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]