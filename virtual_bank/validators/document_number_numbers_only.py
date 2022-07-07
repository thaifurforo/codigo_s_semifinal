from typing import Union

def document_number_numbers_only_validate(document_number: Union[str, int]) -> bool:
  return document_number.isnumeric()
    