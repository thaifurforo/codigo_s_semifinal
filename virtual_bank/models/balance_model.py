from django.db import models, IntegrityError
from django.dispatch import receiver
from virtual_bank.models.account_model import Account
from virtual_bank.models.transaction_model import Transaction


class Balance(models.Model):

    account_number = models.OneToOneField(
        Account, on_delete=models.CASCADE, primary_key=True)
    balance = models.FloatField(default=0)

    @receiver(models.signals.post_save, sender=Account)
    def add_account(sender, instance, created, **kwargs):
        if created:
            try:
                Balance.objects.create(account_number=instance)
            except IntegrityError:
                pass

    @receiver(models.signals.post_save, sender=Transaction)
    def add_transaction(sender, instance, **kwargs):
        if instance.debit_account:
            account_debits = sum([i[0] for i in Transaction.objects.filter(
                debit_account=instance.debit_account).values_list('amount')])
            account_credits = sum([i[0] for i in Transaction.objects.filter(
                credit_account=instance.debit_account).values_list('amount')])
            Balance.objects.filter(pk=instance.debit_account).update(
                balance=(round(account_credits-account_debits, 2)))
        if instance.credit_account:
            account_debits = sum([i[0] for i in Transaction.objects.filter(
                debit_account=instance.credit_account).values_list('amount')])
            account_credits = sum([i[0] for i in Transaction.objects.filter(
                credit_account=instance.credit_account).values_list('amount')])
            Balance.objects.filter(pk=instance.credit_account).update(
                balance=(round(account_credits-account_debits, 2)))
