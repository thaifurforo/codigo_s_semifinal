from django.db import models, IntegrityError
from django.dispatch import receiver
from virtual_bank.models.account_model import Account
from virtual_bank.models.transaction_model import Transaction


class Balance(models.Model):
    """This class sets up the 'balance' dataset model, which is ment to calculate
    the current balance in each account.
    It's composed by:

    account = a OneToOneField for the model class Account, and stabilshes that the
    Balance object will be deleted on CASCADE if the Account is deleted (though it's
    not possible to make DELETE requests for the accounts through the API)

    balance = a FloatField to register the value of the current balance for each 
    account - default is 0 since the balance is 0 when the account is first opened
    """

    account = models.OneToOneField(
        Account, on_delete=models.CASCADE, primary_key=True)
    balance = models.FloatField(default=0, editable=False)

    @receiver(models.signals.post_save, sender=Account)
    def add_account(sender, instance, created, **kwargs):
        """This function creates a post_save signal that creates a instance on the
        Balance model database everytime a account is added to the Account model
        database.
        """
        if created:
            try:
                Balance.objects.create(account=instance)
            except IntegrityError:
                pass

    @receiver([models.signals.post_save, models.signals.post_delete], sender=Transaction)
    def add_transaction(sender, instance, **kwargs):
        """This function creates a post_save and a post_delete signal that updates
        the balance field of the Balance object nested to the debit account and
        of the Balance object nested to the credit account, everytime a transaction
        is created or deleted, for the sum of every credit transaction the account
        has ever received minus the sum of every debit transaction the account has
        ever made.
        """
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
