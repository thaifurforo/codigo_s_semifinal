"""Module that contains the Address Model Class.
"""

from django.db import IntegrityError, models
from django.core.validators import RegexValidator
from django.dispatch import receiver
from pycep_correios import get_address_from_cep, WebService
from virtual_bank.models.customer_model import Customer


class Address(models.Model):
    """This class sets up the 'address' dataset model, which is ment to avoid duplicates
    on the addresses registrations and an unnecessary enlargment of the database.
    It's composed by:

    zip_code -> a CharField containing the zip code for the address

    city -> a CharField containing the name of the city to which this zip code
    refers to

    district -> a CharField containing the initials to the name of the district
    to which this zip code refers to

    neightborhood -> a CharField containing the name of the neighborhood to which
    this zip code refers to

    street -> a CharField containing the name of the street to which this zip code
    refers to
    """

    zip_code = models.CharField(
        verbose_name='CEP',
        unique=True,
        help_text='Formato: 00.000-000',
        validators=[
            RegexValidator('[0-9]{5}-[0-9]{3}',
                           message='Formato de CEP inválido')
        ],
        max_length=9,
    )
    city = models.CharField(verbose_name='Cidade', default='', max_length=80)
    district = models.CharField(
        verbose_name='Estado', max_length=2, default='')
    neighborhood = models.CharField(
        verbose_name='Bairro', default='', max_length=80)
    street = models.CharField(
        verbose_name='Logradouro', default='', max_length=100)

    def save(self, *args, **kwargs):
        """This function overrides the save method for this Class to get the data
        for the address' fields, based on the zip_code, using the library
        'pycep-correios' to get the data from VIACEP API.
        """

        zip_data = get_address_from_cep(
            self.zip_code, webservice=WebService.VIACEP)
        self.city = zip_data['cidade']
        self.district = zip_data['uf']
        self.neighborhood = zip_data['bairro']
        self.street = zip_data['logradouro']
        super().save(*args, **kwargs)

    @receiver(models.signals.post_save, sender=Customer)
    def add_address(sender, instance, **kwargs):
        """This function creates a post_save signal that creates a instance on the
        address model database everytime a customer is added or updated to the
        customer model database.
        If the zip_code informed on the customer POST, PUT or PATCH request already
        exists on the address model database, it will pass, avoiding duplicates.
        """

        try:
            Address.objects.create(zip_code=instance.zip_code)
        except IntegrityError:
            pass
