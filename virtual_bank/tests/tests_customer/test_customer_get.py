"""Module that contains the TestCustomerGet Class.
"""

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from virtual_bank.models import Customer


class TestCustomerGet(APITestCase):
    """This Class sets tests for the GET request on Customer objects
    """

    def setUp(self) -> None:
        """This method sets up the tests for this Class
        """

        # Given
        self.customer = {
            "customer_type": "PF",
            "document_number": "12345678909",
            "name": "Fulano de Tal",
            "phone_number": "+55 11 99999-9999",
            "email": "fulano@email.com.br",
            "birthdate": "2000-01-01",
            "zip_code": "02039-000",
            "door_number": "100",
            "complement": None,
        }

        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)
        post = self.client.post(
            '/v1/customer/', self.customer, format='json')

    def test_customer_get_request_successful(self):
        """This method tests if the customer GET requests return a success response
        """

        # When
        response = self.client.get('/v1/customer/')

        # Then
        self.assertEqual(response.status_code, 200)

    def test_customer_get_results_count(self):
        """This method tests if the customer GET requests return the correct number
        of itens
        """

        # When
        customer_get = self.client.get(
            '/v1/customer/', format='json').data.items()
        get_dict = {}
        for key, values in customer_get:
            get_dict[key] = values

        # Then
        self.assertEqual(get_dict['count'], 1)

    def test_customer_get_document_number(self):
        """This method tests if the customer GET requests return the correct data
        on document_number field
        """

        # When
        customer_get = Customer.objects.get(name="Fulano de Tal")

        # Then
        self.assertEqual(
            customer_get.document_number, self.customer['document_number']
        )
