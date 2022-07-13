def inactive_account_if_closure_date_validate(closure_date, active_account: bool) -> bool:
    '''There can only be an closure date if the account is set as inactive'''
    if active_account and closure_date != None:
        return False
    else:
        return True


def closure_date_if_inactive_account_validate(closure_date, conta_ativa: bool) -> bool:
    '''The account can only be set as innactive if a closure date is informed'''
    if not conta_ativa and closure_date == None:
        return False
    else:
        return True


def inactive_account_if_balance_zero(active_account: bool, balance: float) -> bool:
    '''It's only possible to inactivate an account if the current balance is equal to 0'''
    if active_account == False and balance != 0.0:
        return False
    else:
        return True


def activate_account_after_inactivated(update_active_account, current_active_account):
    """Returns True if the client is trying to update the active_account field value
    to True and it's already False (meaning they're trying to reactivate the account,
    which shouldn't be possible"""
    return update_active_account == True and current_active_account == False
