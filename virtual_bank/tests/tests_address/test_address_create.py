from django.test import TransactionTestCase
from virtual_bank.models import Customer, Address
from pycep_correios import get_address_from_cep, WebService


class TestAddressCreate(TransactionTestCase):
    def setUp(self) -> None:

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

        customer = Customer.objects.create(
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

        self.customer = Customer.objects.create(
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

        # When
        address = Address.objects.get(zip_code=self.customer.zip_code)
        zip_data = get_address_from_cep(
            self.customer.zip_code, webservice=WebService.VIACEP
        )

        # Then
        self.assertEqual(address.street, zip_data['logradouro'])

    def test_multiple_addresses_created(self):

        # When
        address_count = Address.objects.count()

        # Then
        self.assertEqual(address_count, 2)
