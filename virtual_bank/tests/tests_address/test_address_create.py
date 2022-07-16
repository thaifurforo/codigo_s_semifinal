"""Module that contains the TestAddressCreate Class.
"""


from django.test import TransactionTestCase
from pycep_correios import get_address_from_cep, WebService
from virtual_bank.models import Customer, Address


class TestAddressCreate(TransactionTestCase):
    """This Class sets tests for the creation of Address objects
    """

    def setUp(self) -> None:
        """This method sets up the tests for this Class
        """

        # Given
        self.customer1 = Customer.objects.create(
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

        self.customer2 = Customer.objects.create(
            customer_type="PJ",
            document_number="12345678000954",
            name="XPTO Ltda",
            phone_number="+55 21 3333-3333",
            email="contato@xpto.com",
            birthdate=None,
            zip_code="02039-000",
            door_number="987",
            complement=None,
        )

        self.customer3 = Customer.objects.create(
            customer_type="PF",
            document_number="98765432100",
            name="Fulano de Tal",
            phone_number="+55 11 98888-8888",
            email="fulano@seuemail.com",
            birthdate="1990-12-12",
            zip_code="45428-000",
            door_number="987",
            complement=None,
        )

    def test_address_created(self):
        """This method tests if the street field on the created addresses
        are being accessed correctly
        """

        # When
        address1 = Address.objects.get(zip_code=self.customer1.zip_code)
        zip_data1 = get_address_from_cep(
            self.customer1.zip_code, webservice=WebService.VIACEP
        )

        address2 = Address.objects.get(zip_code=self.customer2.zip_code)
        zip_data2 = get_address_from_cep(
            self.customer2.zip_code, webservice=WebService.VIACEP
        )

        address3 = Address.objects.get(zip_code=self.customer3.zip_code)
        zip_data3 = get_address_from_cep(
            self.customer3.zip_code, webservice=WebService.VIACEP
        )

        # Then
        self.assertEqual(address1.street, zip_data1['logradouro'])
        self.assertEqual(address2.street, zip_data2['logradouro'])
        self.assertEqual(address3.street, zip_data3['logradouro'])

    def test_multiple_addresses_created(self):
        """This method tests if the addresses on the set up were created, noting
        that the duplicate addresses should be instanced only once
        """

        # When
        address_count = Address.objects.count()

        # Then
        self.assertEqual(address_count, 2)
