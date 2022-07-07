from os import access
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from models import Account
from serializers import AccountSerializer

# Create your views here.
class ContaViewSet(viewsets.ModelViewSet):
  queryset = Account.objects.all()
  serializer_class = AccountSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]
