from tabnanny import verbose
from django.db import models
from django.utils import timezone
from virtual_bank.models.account_model import Account


class Transaction(models.Model):

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
