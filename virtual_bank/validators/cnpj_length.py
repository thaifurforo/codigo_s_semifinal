from typing import Union

def cnpj_length_validate(document_number: Union[str, int]) -> bool:
  """Verifica se o campo CNPJ tem 14 caracteres"""
  return len(str(document_number)) == 14
