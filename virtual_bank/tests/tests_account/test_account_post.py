"""Module that contains the TestAccountPost Class.
"""

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from virtual_bank.models import Customer


class TestAccountPost(APITestCase):
    """This Class sets tests for the POST request on Account objects
    """

    def setUp(self) -> None:
        """This method sets up the tests for this Class
        """

        # Given
        self.customer = Customer.objects.create(
            customer_type="PF",
            document_number="12345678909",
            name="Ciclano de Tal",
            phone_number="+55 11 99999-9999",
            email="ciclano@email.com.br",
            birthdate="2000-01-01",
            zip_code="02039-000",
            door_number="100",
            complement=None,
        )

        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)

    def test_account_post_sucessfull(self):
        """This method tests if the accounts POST requests return a success response
        """

        # When
        account = {
            "customer": self.customer.id,
            "opening_date": "2022-01-01",
            "active_account": True,
            "closure_date": None,
        }

        response = self.client.post('/v1/account/', account, format='json')

        # Then
        self.assertEqual(response.status_code, 201)
