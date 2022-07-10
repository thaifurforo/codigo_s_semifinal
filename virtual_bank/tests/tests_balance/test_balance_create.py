from django.test import TestCase
from virtual_bank.models import Account, Balance, Customer


class TestBalanceCreate(TestCase):

    def setUp(self) -> None:

        # Given
        customer = Customer.objects.create(customer_type="PF",
                                           document_number="12345678909",
                                           name="Ciclano de Tal",
                                           phone_number="+55 11 99999-9999",
                                           email="ciclano@email.com.br",
                                           birthdate="2000-01-01",
                                           zip_code="02039-000",
                                           door_number="100",
                                           complement=None
                                           )

        Account.objects.create(customer=customer,
                                          opening_date="2022-01-01",
                                          active_account=True,
                                          closure_date=None
                                          )

        Account.objects.create(customer=customer,
                                          opening_date="2022-02-01",
                                          active_account=True,
                                          closure_date=None
                                          )
        Account.objects.create(customer=customer,
                                          opening_date="2022-03-01",
                                          active_account=True,
                                          closure_date=None
                                          )


    def test_balance_created(self):

        # When
        account = Account.objects.get(id=1)
        balance = Balance.objects.get(account=account)

        # Then
        self.assertEqual(balance.balance, 0)


    def test_multiple_balances_created(self):

        # When
        balance_count = Balance.objects.count()

        # Then
        self.assertEqual(balance_count, 3)