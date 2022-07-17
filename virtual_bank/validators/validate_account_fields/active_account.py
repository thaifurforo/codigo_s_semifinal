"""Module that contains the validators for the active_account field from the Account serializer.
"""


def inactive_account_if_closure_date_validate(
    closure_date, active_account: bool
) -> bool:
    """Checks if the client is trying to set a closure_date to an active account

    Args:
        closure_date (datetime.date): Account's closure date set by the client
        active_account (bool): Account's active status set by the client

    Returns:
        bool: Returns False if the account is active and there is a closure_date
        different than null set by the client
    """
    if active_account and closure_date != None:
        return False
    else:
        return True


def inactive_account_if_balance_zero(active_account: bool, balance: float) -> bool:
    """Checks if the client is trying to inactivate an account which balance
    isn't equal to 0, which shouldn't be possible

    Args:
        active_account (bool): Account's active status set by the client
        balance (float): Account's current balance

    Returns:
        bool: Returns False if the account is inactive and the balance is not
        equal to 0
    """
    if active_account == False and balance != 0.0:
        return False
    else:
        return True


def activate_account_after_inactivated(
    update_active_account: bool, current_active_account: bool
) -> bool:
    """Checks if the client is trying to reactivate an account that was already
    innactivated (closed), which shouldn't be possible

    Args:
        update_active_account (bool): The active_account field set in the update request (PUT or PATCH)
        current_active_account (bool): The active_account field saved in the object instance

    Returns:
        bool: Returns True if the updated_active_account is True and the
        current_active_account is False
    """
    return update_active_account == True and current_active_account == False
