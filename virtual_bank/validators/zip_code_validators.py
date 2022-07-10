from pycep_correios import get_address_from_cep, WebService, exceptions


def zip_code_format_valid(zip_code: str) -> bool:
    try:
        get_address_from_cep(zip_code, webservice=WebService.VIACEP)
        return True
    except exceptions.InvalidCEP:
        return False
    except exceptions.BaseException:
        return True


def zip_code_not_found(zip_code: str) -> bool:
    try:
        get_address_from_cep(zip_code, webservice=WebService.VIACEP)
        return True
    except exceptions.CEPNotFound:
        return False
    except exceptions.BaseException:
        return True
