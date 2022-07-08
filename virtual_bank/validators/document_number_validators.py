from typing import Union
from utilities import create_check_digit_module_11

def document_number_numbers_only_validate(document_number: Union[str, int]) -> bool:
  return document_number.isnumeric()
    

def cnpj_check_digit_validate(document_number: Union[str, int]) -> bool:

    cpf_cnpj_sem_dv = document_number[0:-2]
    pesos = [2, 3, 4, 5, 6, 7, 8, 9]
    dv1 = create_check_digit_module_11(cpf_cnpj_sem_dv, pesos, reverse=True)
    cpf_cnpj_dv1 = str(cpf_cnpj_sem_dv)+str(dv1)
    dv2 = create_check_digit_module_11(cpf_cnpj_dv1, pesos, reverse=True)
    cpf_cnpj_dv = str(cpf_cnpj_dv1)+str(dv2)
    return cpf_cnpj_dv == document_number


def cnpj_length_validate(document_number: Union[str, int]) -> bool:
  """Verifica se o campo CNPJ tem 14 caracteres"""
  return len(str(document_number)) == 14


def cpf_check_digit_validate(document_number: Union[str, int]) -> bool:

    document_number_sem_dv = document_number[0:-2]
    pesos = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    dv1 = create_check_digit_module_11(document_number_sem_dv, pesos)
    document_number_dv1 = str(document_number_sem_dv)+str(dv1)
    pesos = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    dv2 = create_check_digit_module_11(document_number_dv1, pesos)
    document_number_dv = str(document_number_dv1)+str(dv2)
    return document_number_dv == document_number

def cpf_length_validate(document_number: Union[str, int]) -> bool:
  """Verifica se o campo CPF tem 11 caracteres"""
  return len(str(document_number)) == 11