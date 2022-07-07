def closure_date_greater_then_opening_date_validate(closure_date, opening_date) -> bool:
  '''Só poderá haver data de encerramento se a conta estiver marcacda como inativa'''
  if closure_date:
    return closure_date > opening_date
  else:
    return True
