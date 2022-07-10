from django.test import TestCase
from virtual_bank.models import Customer

class TestCustomerCreate(TestCase):
    
    def setUp(self) -> None:
                # Given
        Customer.objects.create(customer_type="PF",
                                document_number="12345678909",
                                name="Ciclano de Tal",
                                phone_number="+55 11 99999-9999",
                                email="ciclano@email.com.br",
                                birthdate="2000-01-01",
                                zip_code="02039-000",
                                door_number="100",
                                complement=None
                                )

   

    def test_customer_create(self):

        # When
        customer = Customer.objects.get(document_number='12345678909')

        # Then
        self.assertEqual(customer.name, "Ciclano de Tal")

   