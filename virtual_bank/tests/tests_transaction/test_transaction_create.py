"""Module that contains the TestTransactionCreate Class.
"""

from django.test import TestCase
from virtual_bank.models import Account, Balance, Customer, Transaction


class TestTransactionCreate(TestCase):
    """This Class sets tests for the creation of Transaction objects
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

        account = Account.objects.create(
            customer=customer,
            opening_date="2022-01-01",
            active_account=True,
            closure_date=None,
        )

        Transaction.objects.create(
            transaction_type='DE',
            date="2022-02-01",
            amount=10,
            debit_account=None,
            credit_account=account,
        )

        Transaction.objects.create(
            transaction_type='SQ',
            date="2022-02-02",
            amount=5,
            debit_account=account,
            credit_account=None,
        )

    def test_transactions_created(self):
        """This method tests if the transactions on the set up was created
        """

        # When
        transactions_count = Transaction.objects.count()

        # Then
        self.assertEqual(transactions_count, 2)

    def test_transaction_amount(self):
        """This method tests if the amount field on the created transaction
        is being accessed correctly
        """

        # When
        transaction = Transaction.objects.get(id=1)

        # Then
        self.assertEqual(transaction.amount, 10)

    def test_transactions_resulting_balance(self):
        """This method tests if the balance field is being correctly updated when
        the transactions are created
        """

        # When
        account = Account.objects.get()
        balance = Balance.objects.get(account=account)

        # Then
        self.assertEqual(balance.balance, 5)
