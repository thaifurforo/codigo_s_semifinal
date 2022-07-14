from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class TestCustomerPost(APITestCase):

    customer = {
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

    def setUp(self) -> None:

        # Given
        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)

    def test_customer_post_request_successful(self):

        # When
        response = self.client.post(
            '/customer/', self.__class__.customer, format='json'
        )

        # Then
        self.assertEqual(response.status_code, 201)
