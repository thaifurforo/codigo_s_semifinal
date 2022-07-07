def closure_date_greater_then_opening_date_validate(data_encerramento, data_abertura) -> bool:
  '''Só poderá haver data de encerramento se a conta estiver marcacda como inativa'''
  return data_encerramento > data_abertura
