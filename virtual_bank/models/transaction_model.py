from django.db import models
from django.utils import timezone
from virtual_bank.models import Account


class Transaction(models.Model):
    """This class sets up the 'transaction' dataset model, composed by:

    transaction_type -> a CharField that refers to the type of transaction, between
    six possible choices: 'TI' (transfer between accounts from the same bank), 
    'TE' (transfer to an account on other bank), 'DE' (deposit), 'RE' (amount received
    in the account), 'PG' (payment of bank slip), 'SQ' (withdraw)

    date -> a DateField that refers to the date in which the transaction was made

    debit_account -> a ForeignKey referring to a Account object that refers to the
    account in which the transaction amount was debited (if so)

    debit_account -> a ForeignKey referring to a Account object that refers to the
    account in which the transaction amount was credited (if so)

    amount -> a FloatField that refers to the amount of the transaction
    """

    TRANSACTION_TYPES = [
        ('TI', 'Transferência entre contas do mesmo banco'),
        ('TE', 'Transferência para outro banco'),
        ('DE', 'Depósito'),
        ('RE', 'Recebimento em conta'),
        ('PG', 'Pagamento de guia ou boleto'),
        ('SQ', 'Saque')
    ]
    transaction_type = models.CharField(verbose_name='Tipo de transação',
                                        choices=TRANSACTION_TYPES, max_length=2, default='TI')
    date = models.DateField(verbose_name='Data', default=timezone.now())
    debit_account = models.ForeignKey(
        Account, null=True, blank=True, on_delete=models.CASCADE, related_name='debit_account', verbose_name='Conta debitada')
    credit_account = models.ForeignKey(
        Account, null=True, blank=True, on_delete=models.CASCADE, related_name='credit_account', verbose_name='Conta creditada')
    amount = models.FloatField(default=0, verbose_name='Valor da transação')
