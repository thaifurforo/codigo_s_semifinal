from django.db import IntegrityError, models
from django.core.validators import RegexValidator
from django.dispatch import receiver
from virtual_bank.models.customer_model import Customer
from pycep_correios import get_address_from_cep, WebService

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

    zip_code = models.CharField(verbose_name='CEP', unique=True, help_text='Formato: 00.000-000', validators=[
                                RegexValidator('[0-9]{5}-[0-9]{3}', message='Formato de CEP inválido')], max_length=9)
    city = models.CharField(verbose_name='Cidade', default='', max_length=80)
    district = models.CharField(
        verbose_name='Estado', max_length=2, default='')
    neighborhood = models.CharField(
        verbose_name='Bairro', default='', max_length=80)
    street = models.CharField(
        verbose_name='Logradouro', default='', max_length=100)

    def save(self, *args, **kwargs):
        zip_data = get_address_from_cep(
            self.zip_code, webservice=WebService.VIACEP)
        self.city = zip_data['cidade']
        self.district = zip_data['uf']
        self.neighborhood = zip_data['bairro']
        self.street = zip_data['logradouro']
        super().save(*args, **kwargs)

    @receiver(models.signals.post_save, sender=Customer)
    def add_address(sender, instance, **kwargs):
        try:
            Address.objects.create(zip_code=instance.zip_code)
        except IntegrityError:
            pass
            # zip_data = get_address_from_cep(instance.zip_code, webservice=WebService.VIACEP)
            # Address.objects.filter(pk=instance.zip_code).update(city=zip_data['cidade'], district=zip_data['uf'], neighborhood=zip_data['bairro'], street=zip_data['logradouro'])
