import random
from django.utils import timezone
from django.core.validators import MaxValueValidator, EmailValidator, RegexValidator
from django.db import models
from banco_digital.validators import check_digit_module_11

# Create your models here.

class Cliente(models.Model):
  PESSOA_FISICA = 'PF'
  PESSOA_JURIDICA = 'PJ'
  TIPO_CHOICES = [(PESSOA_FISICA, 'Física'), (PESSOA_JURIDICA, 'Jurídica')]
  
  tipo = models.CharField(max_length=2, choices=TIPO_CHOICES, default=PESSOA_FISICA)
  cpf_cnpj = models.CharField(verbose_name='CPF/CNPJ', help_text='Somente números', default=0, unique=True, max_length=14, validators=[RegexValidator('[0-9]{11,14}')])
  nome_razao_social = models.CharField(verbose_name='Nome completo ou Razão social', max_length= 80, default='')
  endereco = models.CharField(verbose_name='Endereço completo', max_length= 100, default='')
  telefone = models.CharField(verbose_name='Telefone', help_text='Formato: +DI (DDD) 00000-0000', max_length=20, default='', validators=[RegexValidator('\+[0-9]{2} \(0[0-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}-[0-9]{4}', message='Telefone em formato inválido')])
  email = models.CharField(verbose_name='E-mail', max_length=50, default='', validators=[EmailValidator()])
  data_nascimento = models.DateField(verbose_name='Data de nascimento', null=True, blank=True)

  def __str__(self):
    return self.nome_razao_social

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