"""Module with the validators for the zip_code field from the Customer serializer.
"""

from pycep_correios import get_address_from_cep, WebService, exceptions


def zip_code_format_valid(zip_code: str) -> bool:
    """Checks if the zip code set by the client has a valid format, which should
    be 00000-000 (five numbers, dash, three numbers)

    Args:
        zip_code (str): Zip code set by the client

    Returns:
        bool: Returns True if the zip_code field is in a valid format
    """

    try:
        get_address_from_cep(zip_code, webservice=WebService.VIACEP)
        return True
    except exceptions.InvalidCEP:
        return False
    except exceptions.BaseException:
        return True


def zip_code_found(zip_code: str) -> bool:
    """Checks if the zip code set by the client exists, according to the VIACEP
    API database

    Args:
        zip_code (str): Zip code set by the client

    Returns:
        bool: Return True if the zip_code field exists
    """
    try:
        get_address_from_cep(zip_code, webservice=WebService.VIACEP)
        return True
    except exceptions.CEPNotFound:
        return False
    except exceptions.BaseException:
        return True
