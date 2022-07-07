from typing import Union
import check_digit_module_11

def cpf_check_digit_validate(document_number: Union[str, int]) -> bool:

    document_number_sem_dv = document_number[0:-2]
    pesos = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    dv1 = check_digit_module_11(document_number_sem_dv, pesos)
    document_number_dv1 = str(document_number_sem_dv)+str(dv1)
    pesos = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    dv2 = check_digit_module_11(document_number_dv1, pesos)
    document_number_dv = str(document_number_dv1)+str(dv2)
    return document_number_dv == document_number