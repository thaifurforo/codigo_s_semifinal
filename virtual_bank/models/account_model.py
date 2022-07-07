import random
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.db import models
from validators import check_digit_module_11
from models import Customer

# Create your models here.

class Account(models.Model):
  seed = models.AutoField(primary_key=True, editable=False)
  account_number_no_cd = models.IntegerField(unique=True, verbose_name='Número da conta sem dígito verificador', validators=[MaxValueValidator(999999)], default=0, editable=False)
  check_digit = models.IntegerField(verbose_name='Dígito verificador do número conta', default=0, editable=False)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  active_account = models.BooleanField(default=True)
  balance = models.FloatField(default=0, editable=False)
  opening_date = models.DateField(verbose_name='Data de abertura', default=timezone.now())
  closure_date = models.DateField(verbose_name='Data de encerramento', null=True, blank=True)

  def save(self, *args, **kwargs):
    random.seed = self.seed
    self.account_number_no_cd = str(random.randint(1, 999999)).zfill(6)
    self.check_digit = str(check_digit_module_11(self.account_number_no_cd, [2, 3, 4, 5, 6, 7, 8, 9], reverse=True))
    super().save(*args, **kwargs)
  
  @property
  def account_complete_number(self):
    numero_conta = f'{self.account_number_no_cd}-{self.check_digit}'
    return numero_conta
  
  def __str__(self):
    return self.account_complete_number