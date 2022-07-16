"""This module is used to configure the application
"""

from django.apps import AppConfig


class VirtualBankConfig(AppConfig):
    """This Class sets the configuration for the Virtual Bank app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'virtual_bank'
