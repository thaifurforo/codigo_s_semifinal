"""Module that contains the Account Model Class.
"""

import random
from django.utils import timezone
from django.db import models
from virtual_bank.models.customer_model import Customer
from virtual_bank.validators import create_check_digit_module_11


class Account(models.Model):
    """This class sets up the 'account' dataset model, composed by:

    account_number -> a unique and not editable CharField created by the junction
    of the a generated randomly 6 digit number using the account id (AutoField) as the seed,
    followed by a dash and a check digit, generated using the create_check_digit_module_11
    function, based on the 6 previous digits

    customer -> a ForeignKey for the model class Customer, which refers to the account
    owner and is set to null if the customer's data is removed from the database (based
    on the data protection laws) - it's not set to delete on cascade, because the account
    data, including it's transactions, must remain registered in the virtual_bank database,
    even if the account is closed (set to innactive on active_account field)and the
    customer's data is deleted, since it affects other accounts' data, and also for
    legal reasons that may dictate that records must be kept

    active_account -> a BooleanField which sets if the account is active or if it was closed

    opening_date -> a DateField to register the date the account was opened

    closure_date -> a DateField to register the date the account was closed, if it did
    """

    account_number = models.CharField(
        verbose_name='Número da conta',
        max_length=8,
        default='',
        editable=False,
        unique=True,
    )
    customer = models.ForeignKey(
        Customer, verbose_name='Cliente', on_delete=models.SET_NULL, null=True
    )
    active_account = models.BooleanField(
        verbose_name='Conta ativa', default=True)
    opening_date = models.DateField(
        verbose_name='Data de abertura', default=timezone.now()
    )
    closure_date = models.DateField(
        verbose_name='Data de encerramento', null=True, blank=True
    )

    def save(self, *args, **kwargs):
        """This method overrides the save method from this Class to make the
        necessaries calculations to generate the account_number.
        """

        random.seed = self.id
        account_number_no_cd = str(random.randint(1, 999999)).zfill(6)
        check_digit = str(
            create_check_digit_module_11(
                account_number_no_cd, [9, 8, 7, 6, 5, 4]
            )
        )
        self.account_number = f'{account_number_no_cd}-{check_digit}'
        super().save(*args, **kwargs)

    def __str__(self):
        """This method overrides the __str__ method for this Class to determinate
        that the representation of the account model in the graphic interfaces
        of the application will be the account_number field.
        """

        return self.account_number