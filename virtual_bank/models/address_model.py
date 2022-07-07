from django.db import IntegrityError, models
from django.core.validators import RegexValidator
from django.dispatch import receiver
from virtual_bank.models.customer_model import Customer

# Create your models here.
class Address(models.Model):

  # DISTRICTS = [
  #   ('AC', 'Acre'),
  #   ('AL', 'Alagoas'), 
  #   ('AP', 'Amapá'),
  #   ('AM', 'Amazonas'),
  #   ('BA', 'Bahia'),
  #   ('CE', 'Ceará'),
  #   ('DF', 'Distrito Federal'),
  #   ('ES', 'Espírito Santo'),
  #   ('GO', 'Goiás'),
  #   ('MA', 'Maranhão'),
  #   ('MT', 'Mato Grosso'),
  #   ('MS', 'Mato Grosso do Sul'),
  #   ('MG', 'Minas Gerais'),
  #   ('PA', 'Pará'),
  #   ('PB', 'Paraíba'),
  #   ('PR', 'Paraná'),
  #   ('PE', 'Pernambuco'),
  #   ('PI', 'Piauí'),
  #   ('RJ', 'Rio de Janeiro'),
  #   ('RN', 'Rio Grande do Norte'),
  #   ('RS', 'Rio Grande do Sul'),
  #   ('RO', 'Rondônia'),
  #   ('RR', 'Roraima'),
  #   ('SC', 'Santa Catarina'),
  #   ('SP', 'São Paulo'),
  #   ('SE', 'Sergipe'),
  #   ('TO', 'Tocantins')
  #   ]

  zip_code = models.CharField(primary_key=True, help_text='Formato: 00.000-000', validators=[RegexValidator('[0-9]{2}.[0-9]{3}-[0-9]{3}')], max_length=10)
  # city = models.CharField(default='', max_length=50)
  # district = models.CharField(choices=DISTRICTS, max_length=2, default='AC')
  # neighborhood = models.CharField(default='', max_length=50)
  # street = models.CharField(default='', max_length=100)

  @receiver(models.signals.post_save, sender=Customer)
  def add_address(sender, instance, created, **kwargs):
      if created:
          try:
            Address.objects.create(zip_code=instance.zip_code)
          except IntegrityError:
            pass
  
