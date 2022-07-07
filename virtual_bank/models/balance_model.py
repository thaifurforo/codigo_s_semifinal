from django.db import models, IntegrityError
from django.dispatch import receiver
from virtual_bank.models.account_model import Account
from virtual_bank.models.transaction_model import Transaction

class Balance(models.Model):

  account_number = models.CharField(primary_key = True, default='', max_length=8)
  balance = models.FloatField(default=0)

  @receiver(models.signals.post_save, sender=Account)
  def add_account(sender, instance, created, **kwargs):
      if created:
          try:
            Balance.objects.create(account_number=instance.account_number)
          except IntegrityError:
            pass
  
  @receiver(models.signals.post_save, sender=Transaction)
  def add_transaction(sender, instance, created, **kwargs):
      if created:
        if instance.debit_account:
          Balance.objects.filter(pk=instance.debit_account).update(balance=models.F('balance') - instance.amount)
        if instance.credit_account:
          Balance.objects.filter(pk=instance.credit_account).update(balance=models.F('balance') + instance.amount)
        

  