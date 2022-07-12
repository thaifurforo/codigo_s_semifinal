from django.core.validators import EmailValidator, RegexValidator
from django.db import models


class Customer(models.Model):
    """This class sets up the 'customer' dataset model, composed by:

    customer_type -> a CharField that refers to the type of customer, between two
    possible choices: 'PF' (natural person) or 'PJ' (juridical person)

    document_number -> a unique CharField composed only by numbers that refers to
    the customer document number (CPF or CNPJ) - it's a CharField, even though it's
    composed only by numbers, because there can be documents numbers starting with
    a 0, on which case it would be disconsidered if it was an IntegerField

    name -> a CharField that refers to the customer's name or corporate name

    phone_number -> a CharField that refers to the customer's phone number, with
    a format validator by RegexValidator, so that the phone number has a international
    code, regional code and the full personal number

    email -> a CharField that refers to the customer's email address, with a email
    format validator

    birthdate -> a DateField that refers to the customer's birthdate - this field
    should be filled only if the customer is a natural person

    zip_code -> a CharField that refers to the customer's address zip code, with
    a format validator by RegexValidator, and used to retrieve the full address
    data for the customer (city, district, neighborhood and street)

    door_number -> a CharField that referes to the customer's address door number

    complement -> a CharField that can be null, that refers to the customer's
    address complement, if there is one
    """

    TYPE_CHOICES = [('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')]

    customer_type = models.CharField(verbose_name='Tipo de cliente',
                                     max_length=2, choices=TYPE_CHOICES, default='PF')
    document_number = models.CharField(verbose_name='CPF/CNPJ', help_text='Somente números',
                                       default=0, unique=True, max_length=14, validators=[RegexValidator('[0-9]{11,14}')])
    name = models.CharField(
        verbose_name='Nome completo ou Razão social', max_length=80, default='')

    phone_number = models.CharField(verbose_name='Telefone', help_text='Formato: +DI DD 00000-0000', max_length=20, default='', validators=[
                                    RegexValidator('\+[0-9]{2} [0-9]{2} (?:[2-8]|9[1-9])[0-9]{3}-[0-9]{4}', message='Telefone em formato inválido')])
    email = models.CharField(
        verbose_name='E-mail', max_length=50, default='', validators=[EmailValidator()])

    birthdate = models.DateField(
        verbose_name='Data de nascimento', null=True, blank=True)

    zip_code = models.CharField(verbose_name='CEP', help_text='Formato: 00000-000',
                                validators=[RegexValidator('[0-9]{5}-[0-9]{3}')], max_length=9)
    door_number = models.CharField(
        verbose_name='Número (endereço)', default='', max_length=10)
    complement = models.CharField(
        verbose_name='Complemento (endereço)', max_length=30, null=True, blank=True)

    def __str__(self):
        """This function overwrites the __str__ function to determinate that the
        representation of the customer model in the graphic interfaces of the
        application will be the name field.
        """
        return self.name
