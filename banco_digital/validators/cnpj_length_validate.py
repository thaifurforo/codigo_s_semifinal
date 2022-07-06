from typing import Union

def cnpj_length_validate(cpf_cnpj: Union[str, int]) -> bool:
  """Verifica se o campo CNPJ tem 14 caracteres"""
  return len(str(cpf_cnpj)) == 14
