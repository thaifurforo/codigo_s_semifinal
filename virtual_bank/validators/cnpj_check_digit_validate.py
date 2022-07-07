from typing import Union
import check_digit_module_11

def cnpj_check_digit_validate(document_number: Union[str, int]) -> bool:

    cpf_cnpj_sem_dv = document_number[0:-2]
    pesos = [2, 3, 4, 5, 6, 7, 8, 9]
    dv1 = check_digit_module_11(cpf_cnpj_sem_dv, pesos, reverse=True)
    cpf_cnpj_dv1 = str(cpf_cnpj_sem_dv)+str(dv1)
    dv2 = check_digit_module_11(cpf_cnpj_dv1, pesos, reverse=True)
    cpf_cnpj_dv = str(cpf_cnpj_dv1)+str(dv2)
    return cpf_cnpj_dv == document_number