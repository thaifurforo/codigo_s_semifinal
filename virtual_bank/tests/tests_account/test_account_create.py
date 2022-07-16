"""Module that contains the TestAccountCreate Class.
"""

from django.test import TestCase
from virtual_bank.models import Account, Customer


class TestAccountCreate(TestCase):
    """This Class sets tests for the creation of Account objects
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

        Account.objects.create(
            customer=customer,
            opening_date="2022-01-01",
            active_account=True,
            closure_date=None,
        )

        Account.objects.create(
            customer=customer,
            opening_date="2022-02-02",
            active_account=False,
            closure_date="2022-03-01",
        )

    def test_account_created(self):
        """This method tests if the accounts on the set up were created
        """

        # When
        accounts_count = Account.objects.count()

        # Then
        self.assertEqual(accounts_count, 2)

    def test_account_active_account(self):
        """This method tests if the active_account field on the created accounts
        are being accessed correctly
        """

        # When
        account1 = Account.objects.get(opening_date="2022-01-01")
        account2 = Account.objects.get(opening_date="2022-02-02")

        # Then
        self.assertEqual(account1.active_account, True)
        self.assertEqual(account2.active_account, False)
