from typing import Union
from check_digit_module_11 import check_digit_module_11

def cpf_check_digit_validate(cpf_cnpj: Union[str, int]) -> bool:

    cpf_cnpj_sem_dv = cpf_cnpj[0:-2]
    pesos = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    dv1 = check_digit_module_11(cpf_cnpj_sem_dv, pesos)
    cpf_cnpj_dv1 = str(cpf_cnpj_sem_dv)+str(dv1)
    pesos = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    dv2 = check_digit_module_11(cpf_cnpj_dv1, pesos)
    cpf_cnpj_dv = str(cpf_cnpj_dv1)+str(dv2)
    return cpf_cnpj_dv == cpf_cnpj