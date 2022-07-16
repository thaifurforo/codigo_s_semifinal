"""Module that contains the TestCustomerCreate Class.
"""

from django.test import TestCase
from virtual_bank.models import Customer


class TestCustomerCreate(TestCase):
    """This Class sets tests for the creation of Customer objects
    """

    def setUp(self) -> None:
        """This method sets up the tests for this Class
        """

        # Given
        Customer.objects.create(
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

    def test_customer_create_count(self):
        """This method tests if the customer on the set up was created
        """

        # When
        customer_count = Customer.objects.count()

        # Then
        self.assertEqual(customer_count, 1)

    def test_customer_create_name(self):
        """This method tests if the name field on the created customer
        is being accessed correctly
        """

        # When
        customer = Customer.objects.get(document_number='12345678909')

        # Then
        self.assertEqual(customer.name, "Ciclano de Tal")
