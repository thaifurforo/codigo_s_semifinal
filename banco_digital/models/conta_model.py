import random
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.db import models
from banco_digital.validators import check_digit_module_11
from cliente_model import Cliente

# Create your models here.

class Conta(models.Model):
  seed = models.AutoField(primary_key=True, editable=False)
  numero_conta_sem_dv = models.IntegerField(unique=True, verbose_name='Número da conta sem dígito verificador', validators=[MaxValueValidator(999999)], default=0, editable=False)
  digito_verificador = models.IntegerField(verbose_name='Dígito verificador do número conta', default=0, editable=False)
  cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
  conta_ativa = models.BooleanField(default=True)
  saldo = models.FloatField(default=0, editable=False)
  data_abertura = models.DateField(verbose_name='Data de abertura', default=timezone.now())
  data_encerramento = models.DateField(verbose_name='Data de encerramento', null=True, blank=True)

  def save(self, *args, **kwargs):
    random.seed = self.seed
    self.numero_conta_sem_dv = str(random.randint(1, 999999)).zfill(6)
    self.digito_verificador = str(check_digit_module_11(self.numero_conta_sem_dv, [2, 3, 4, 5, 6, 7, 8, 9], reverse=True))
    super().save(*args, **kwargs)
  
  @property
  def numero_completo_conta(self):
    numero_conta = f'{self.numero_conta_sem_dv}-{self.digito_verificador}'
    return numero_conta
  
  def __str__(self):
    return self.numero_completo_conta