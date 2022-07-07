from typing import Union

def cpf_length_validate(cpf_cnpj: Union[str, int]) -> bool:
  """Verifica se o campo CPF tem 11 caracteres"""
  return len(str(cpf_cnpj)) == 11