"""Module that contains the validators for the date field from the Transaction serializer.
"""


def transaction_date_more_recent_than_account_opening_date(
    transaction_date, account_opening_date
) -> bool:
    """Checks if the date of the transaction set by the client is more recent than
    the opening date, as there shouldn't be possible to create transactions on
    dates before the account have been opened

    Args:
        transaction_date (datetime.date): Transaction date set by the client
        account_opening_date (datetime.date): Opening date of the Account object related
        to the transaction

    Returns:
        bool: Returns true if the Transaction's date field is greater (more recent)
        than the Account's opening_date field
    """

    return transaction_date >= account_opening_date


