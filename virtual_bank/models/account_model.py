import random
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.db import models
# from django.dispatch import receiver
from virtual_bank.models.customer_model import Customer
from virtual_bank.validators import create_check_digit_module_11


# Create your models here.

class Account(models.Model):
  seed = models.AutoField(primary_key=True, editable=False)
  account_number = models.CharField(max_length=8, default='', editable=False)
  account_number_no_cd = models.IntegerField(unique=True, verbose_name='Número da conta sem dígito verificador', validators=[MaxValueValidator(999999)], default=0, editable=False)
  check_digit = models.IntegerField(verbose_name='Dígito verificador do número conta', default=0, editable=False)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  active_account = models.BooleanField(default=True)
  opening_date = models.DateField(verbose_name='Data de abertura', default=timezone.now())
  closure_date = models.DateField(verbose_name='Data de encerramento', null=True, blank=True)

  def save(self, *args, **kwargs):
    random.seed = self.seed
    self.account_number_no_cd = str(random.randint(1, 999999)).zfill(6)
    self.check_digit = str(create_check_digit_module_11(self.account_number_no_cd, [2, 3, 4, 5, 6, 7, 8, 9], reverse=True))
    self.account_number = f'{self.account_number_no_cd}-{self.check_digit}'
    super().save(*args, **kwargs)
  
  # @property
  # def account_number(self):
  #   numero_conta = f'{self.account_number_no_cd}-{self.check_digit}'
  #   return numero_conta
  
  def __str__(self):
    return self.account_number

  # @receiver(models.signals.post_save, sender=Transaction)
  # def transaction_to_balance(sender, instance, created, **kwargs):
  #     if not created:
  #       if instance.debit_account:
  #         Account.objects.filter(pk=instance.debit_account).update(balance = models.F('balance') - instance.value)
  #       if instance.credit_account:
  #         Account.objects.filter(pk=instance.debit_account).update(balance = models.F('balance') + instance.value)