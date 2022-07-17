"""Module that contains the validators for the active_account field from 
Accounts nested to the Transaction serializer.
"""


def transaction_in_active_account(active_account: bool) -> bool:
    """Checks if the client is trying to create a transaction for an Account which
    has already been closed (innactive)

    Args:
        active_account (bool): Active status of the Account object related to the
        transaction

    Returns:
        bool: Returns True if the Account object related to the transaction is
        active
    """

    return active_account
