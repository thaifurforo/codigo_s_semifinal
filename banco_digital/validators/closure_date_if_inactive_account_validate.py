def closure_date_if_inactive_account_validate(data_encerramento, conta_ativa: bool) -> bool:
  '''Só poderá haver data de encerramento se a conta estiver marcacda como inativa'''
  if not conta_ativa and data_encerramento == None:
    return False
  else:
    return True
