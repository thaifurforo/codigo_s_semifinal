def inactive_account_if_closure_date_validate(data_encerramento, conta_ativa: bool) -> bool:
  '''Só poderá haver data de encerramento se a conta estiver marcacda como inativa'''
  if conta_ativa and data_encerramento != None:
    return False
  else:
    return True