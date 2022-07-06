from typing import Union

def cpf_cnpj_numbers_only_validate(cpf_cnpj: Union[str, int]) -> bool:
  return cpf_cnpj.isnumeric()
    