"""Module with the validators for the closure_date field from the Account serializer.
"""


def closure_date_more_recent_than_opening_date_validate(
    closure_date, opening_date
) -> bool:
    """Checks if the closure date set for the account is more recent than the
    opening date

    Args:
        closure_date (date): Account's closure date set by the client
        opening_date (date): Account's opening date set by the client

    Returns:
        bool: Returns False if there is a closure_date set and it's less recent
        than the opening_date
    """
    if closure_date:
        return closure_date > opening_date
    else:
        return True


def closure_date_more_recent_than_last_transaction_date(
    last_credit_transaction_date, last_debit_transaction_date, closure_date
) -> bool:
    """_summary_

    Args:
        last_credit_transaction_date (date): Account's last credit transaction date
        last_debit_transaction_date (date): Account's last debit transaction date
        closure_date (date): Account's closure date set by the client

    Returns:
        bool: Returns True if the closure date is more recent than the last debit
        date and the last credit date
    """

    if last_debit_transaction_date:
        closure_date_more_recent_than_last_debit = (
            last_debit_transaction_date <= closure_date
        )
    else:
        closure_date_more_recent_than_last_debit = True

    if last_credit_transaction_date:
        closure_date_more_recent_than_last_credit = (
            last_credit_transaction_date <= closure_date
        )
    else:
        closure_date_more_recent_than_last_credit = True

    return (
        closure_date_more_recent_than_last_debit
        and closure_date_more_recent_than_last_credit
    )
