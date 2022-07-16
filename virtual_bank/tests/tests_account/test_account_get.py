"""Module that contains the TestAccountGet Class.
"""

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from virtual_bank.models import Account, Customer


class TestAccountGet(APITestCase):
    """This Class sets tests for the GET request on Account objects
    """

    def setUp(self) -> None:
        """This method sets up the tests for this Class
        """

        # Given
        customer = Customer.objects.create(
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

        self.account1 = Account.objects.create(
            customer=customer,
            opening_date="2022-01-01",
            active_account=True,
            closure_date=None,
        )

        self.account2 = Account.objects.create(
            customer=customer,
            opening_date="2022-02-02",
            active_account=False,
            closure_date="2022-03-01",
        )

        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)

    def test_account_get_request_successful(self):
        """This method tests if the accounts GET requests return a success response
        """

        # When
        response = self.client.get('/v1/account/')

        # Then
        self.assertEqual(response.status_code, 200)

    def test_account_get_results_count(self):
        """This method tests if the accounts GET requests return the correct number
        of itens
        """

        # When
        account_get = self.client.get('/v1/account/', format='json').data.items()
        get_dict = {}
        for key, values in account_get:
            get_dict[key] = values

        # Then
        self.assertEqual(get_dict['count'], 2)

    def test_account_get_active_account(self):
        """This method tests if the accounts GET requests return the correct data
        on active_account field
        """

        # When
        account1_get = Account.objects.get(id=self.account1.id)
        account2_get = Account.objects.get(id=self.account2.id)

        # Then
        self.assertEqual(account1_get.active_account,
                         self.account1.active_account)
        self.assertEqual(account2_get.active_account,
                         self.account2.active_account)
