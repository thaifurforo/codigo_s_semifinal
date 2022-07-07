from django.core.validators import EmailValidator, RegexValidator
from django.db import models
from django.dispatch import receiver
from models import Address

# Create your models here.

class Customer(models.Model):
  TIPO_CHOICES = [('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')]
  
  client_type = models.CharField(max_length=2, choices=TIPO_CHOICES, default='PF')
  document_number = models.CharField(verbose_name='CPF/CNPJ', help_text='Somente números', default=0, unique=True, max_length=14, validators=[RegexValidator('[0-9]{11,14}')])
  name = models.CharField(verbose_name='Nome completo ou Razão social', max_length= 80, default='')
  address = models.CharField(verbose_name='Endereço completo', max_length= 100, default='')
  phone_number = models.CharField(verbose_name='Telefone', help_text='Formato: +DI (DDD) 00000-0000', max_length=20, default='', validators=[RegexValidator('\+[0-9]{2} \(0[0-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}-[0-9]{4}', message='Telefone em formato inválido')])
  email = models.CharField(verbose_name='E-mail', max_length=50, default='', validators=[EmailValidator()])
  birthdate = models.DateField(verbose_name='Data de nascimento', null=True, blank=True)
  zip_code = models.CharField(help_text='Formato: 00.000-000', validators=[RegexValidator('[0-9]{2}.[0-9]{3}-[0-9]{3}')], max_length=10)
  door_number = models.CharField(default='', max_length=10)
  complement = models.CharField(default='', max_length=30)

  @receiver(models.signals.post_save, sender=Address)
  def add_address(sender, instance, created, **kwargs):
      if created:
          Address.objects.create(zip_code=instance.zip_code)

  def __str__(self):
    return self.name