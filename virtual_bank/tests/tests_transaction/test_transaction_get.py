from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from virtual_bank.models import Account, Customer, Transaction


class TestTransactionGet(APITestCase):
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

        self.account = Account.objects.create(
            customer=customer,
            opening_date="2022-01-01",
            active_account=True,
            closure_date=None,
        )

        self.transaction1 = Transaction.objects.create(
            transaction_type='DE',
            date="2022-02-01",
            amount=10,
            debit_account=None,
            credit_account=self.account,
        )

        self.transaction2 = Transaction.objects.create(
            transaction_type='SQ',
            date="2022-02-02",
            amount=5,
            debit_account=self.account,
            credit_account=None,
        )

        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)

    def test_transaction_get_request_successful(self):

        # When
        response = self.client.get('/transaction/')

        # Then
        self.assertEqual(response.status_code, 200)

    def test_transaction_get_results_count(self):

        # When
        transaction_get = self.client.get('/transaction/', format='json').data.items()
        get_dict = {}
        for key, values in transaction_get:
            get_dict[key] = values

        # Then
        self.assertEqual(get_dict['count'], 2)

    def test_transaction_get_amount(self):

        # When
        transaction1_get = Transaction.objects.get(id=self.transaction1.id)
        transaction2_get = Transaction.objects.get(id=self.transaction2.id)

        # Then
        self.assertEqual(transaction1_get.amount, self.transaction1.amount)
        self.assertEqual(transaction2_get.amount, self.transaction2.amount)
