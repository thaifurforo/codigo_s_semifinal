from rest_framework import serializers


def inactive_account_if_closure_date_validate(data_encerramento, conta_ativa: bool) -> bool:
    '''Só poderá haver data de encerramento se a conta estiver marcacda como inativa'''
    if conta_ativa and data_encerramento != None:
        return False
    else:
        return True


def closure_date_if_inactive_account_validate(data_encerramento, conta_ativa: bool) -> bool:
    '''Só poderá haver data de encerramento se a conta estiver marcacda como inativa'''
    if not conta_ativa and data_encerramento == None:
        return False
    else:
        return True


# def inactive_account_if_balance_zero(active_account: bool, balance: float) -> bool:
#     '''It's only possible to inactivate an account if the current balance is equal to 0'''
#     if active_account == False and balance != 0.0:
#         return False
#     else:
#         return True
