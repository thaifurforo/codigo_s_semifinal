from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from models import Customer
from serializers import CustomerSerializer


# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]