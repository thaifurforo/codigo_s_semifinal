from django.db import models
from django.utils import timezone
from virtual_bank.models.account_model import Account

class Transaction(models.Model):

  TRANSACTION_TYPES = [
    ('TI', 'Transferência entre contas do mesmo banco'),
    ('TE', 'Transferência de/para conta de outro banco'),
    ('DE', 'Depósito'),
    ('RE', 'Recebimento em conta'),
    ('PG', 'Pagamento de guia ou boleto'),
    ('SQ', 'Saque')
  ]
  transaction_type = models.CharField(choices=TRANSACTION_TYPES, max_length=2, default='TI')
  date = models.DateField(default=timezone.now())
  debit_account = models.ForeignKey(Account, null=True, blank=True, on_delete=models.CASCADE, related_name='debit_account')
  credit_account = models.ForeignKey(Account, null=True, blank=True, on_delete=models.CASCADE, related_name='credit_account')
  amount = models.FloatField(default=0)
  


