from django.core.validators import EmailValidator, RegexValidator
from django.db import models

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