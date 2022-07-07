from typing import Union

def cpf_length_validate(document_number: Union[str, int]) -> bool:
  """Verifica se o campo CPF tem 11 caracteres"""
  return len(str(document_number)) == 11