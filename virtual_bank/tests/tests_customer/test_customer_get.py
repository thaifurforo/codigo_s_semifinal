from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from virtual_bank.models import Customer


class TestCustomerGet(APITestCase):

    customer = {
        "customer_type": "PF",
        "document_number": "12345678909",
        "name": "Fulano de Tal",
                "phone_number": "+55 11 99999-9999",
                "email": "fulano@email.com.br",
                "birthdate": "2000-01-01",
                "zip_code": "02039-000",
                "door_number": "100",
                "complement": None
    }

    def setUp(self) -> None:

        # Given
        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)
        post = self.client.post(
            '/customer/', self.__class__.customer, format='json')

    def test_customer_get_request_successful(self):

        # When
        response = self.client.get('/customer/')

        # Then
        self.assertEqual(response.status_code, 200)

    def test_customer_get_results_count(self):

        # When
        customer_get = self.client.get(
            '/customer/', format='json').data.items()
        get_dict = {}
        for key, values in customer_get:
            get_dict[key] = values

        # Then
        self.assertEqual(get_dict['count'],
                         1)

    def test_customer_get_document_number(self):

        # When
        customer_get = Customer.objects.get(name="Fulano de Tal")

        # Then
        self.assertEqual(customer_get.document_number,
                         self.__class__.customer['document_number'])
