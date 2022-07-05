from rest_framework import viewsets
from banco_digital.models import Cliente, Conta
from banco_digital.serializer import ClienteSerializer, ContaSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
  queryset = Cliente.objects.all()
  serializer_class = ClienteSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class ContaViewSet(viewsets.ModelViewSet):
  queryset = Conta.objects.all()
  serializer_class = ContaSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]
