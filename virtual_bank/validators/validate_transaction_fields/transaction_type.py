"""Module with the validators for the transaction_type field from the Transaction serializer.
"""


def debit_transactions_validation(transaction_type: str, debit_account: str) -> bool:
    """Checks if the client set a debit account if the transaction type was one
    of the possible debit transactions: "TI" (transfer between accounts from the
    same bank), "TE" (transfer to an account on other bank), "PG" (payment of
    bank slip) and "SQ" (withdraw), and also if they didn't set one if the
    transaction type was not one of these

    Args:
        transaction_type (str): Transaction type set by the client
        debit_account (str): Debit account set by the client

    Returns:
        bool: Returns True if the transaction_type set is one of the possible
        debit transactions and the client set a value in the debit_account field,
        or if there was no debit_account set and the transaction_type was not any
        of the possible debit transactions
    """
    debit_transaction_types = ['TI', 'TE', 'PG', 'SQ']

    if ((not debit_account) and (transaction_type in debit_transaction_types)) or (
        (debit_account) and not (transaction_type in debit_transaction_types)
    ):
        return False
    else:
        return True


def credit_transactions_validation(transaction_type: str, credit_account: str) -> bool:
    """Checks if the client set a credit account if the transaction type was one
    of the possible credit transactions: "TI" (transfer between accounts from the
    same bank), "DE" (deposit), "RE" (amount received in the account), and also
    if they didn't set one if the transaction type was not one of these

    Args:
        transaction_type (str): Transaction type set by the client
        credit_account (str): Credit account set by the client

    Returns:
        bool: Returns True if the transaction_type set is one of the possible
        credit transactions and the client set a value in the credit_account field,
        or if there was no credit_account set and the transaction_type was not any
        of the possible credit transactions
    """

    credit_transaction_types = ['TI', 'DE', 'RE']

    if ((not credit_account) and (transaction_type in credit_transaction_types)) or (
        (credit_account) and not (transaction_type in credit_transaction_types)
    ):
        return False
    else:
        return True
