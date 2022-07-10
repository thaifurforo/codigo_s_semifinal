from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from virtual_bank.models import Account, Customer


class TestAccountPost(APITestCase):

    def setUp(self) -> None:
        # Given
        self.customer = Customer.objects.create(customer_type="PF",
                                                document_number="12345678909",
                                                name="Ciclano de Tal",
                                                phone_number="+55 11 99999-9999",
                                                email="ciclano@email.com.br",
                                                birthdate="2000-01-01",
                                                zip_code="02039-000",
                                                door_number="100",
                                                complement=None
                                                )

        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)

    def test_account_post_sucessfull(self):

       # When
        account = {"customer": self.customer.id,
                   "opening_date": "2022-01-01",
                   "active_account": True,
                   "closure_date": None}

        response = self.client.post(
            '/account/', account, format='json')

        # Then
        self.assertEqual(response.status_code, 201)
