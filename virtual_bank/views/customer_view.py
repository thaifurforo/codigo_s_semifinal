"""Module that contains the Customer View Set.
"""

from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from virtual_bank.models import Customer
from virtual_bank.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """This class creates a ModelViewSet for the Customer serializer.

    It allows all of the http methods to be used on the requests for this view.

    The queryset determinates that the Customer objects will be shown first by id.

    The serializer class used for this view is the CustomerSerializer.

    There are set some filters for this ViewSet:
    The data can be ordered by name.
    The data can be searched by name and document_number.
    The data can be filtered by selecting the customer_type ('PF' or 'PJ'), and
    by selecting a birthdate (exact, greater than or equal, less than or equal).

    The authentication for this ViewSet is BasicAuthentication, which means that the
    authentication is made through an user an password combination.
    The permission class is IsAuthenticated, which means that it alows access to
    any authenticated user, and denies access to any unauthenticated user.
    """

    queryset = Customer.objects.all().order_by('id')

    serializer_class = CustomerSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    ordering_fields = ['name']
    search_fields = ['name', 'document_number']
    filterset_fields = {
        'customer_type': ['exact'],
        'birthdate': ['exact', 'gte', 'lte'],
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
