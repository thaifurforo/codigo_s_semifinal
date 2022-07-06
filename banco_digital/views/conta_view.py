from rest_framework import viewsets
from banco_digital.models import Conta
from banco_digital.serializers import ContaSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ContaViewSet(viewsets.ModelViewSet):
  queryset = Conta.objects.all()
  serializer_class = ContaSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]
