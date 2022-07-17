"""Module that contains the validators for the debit_account field from the
Transaction serializer.
"""


def credit_transactions_validation(transaction_type: str, credit_account: str) -> bool:
    """Checks if the client didn't set a credit account, which they should, if
    the transaction type was one of the possible credit transactions: "TI" (transfer
    between accounts from the same bank), "DE" (deposit), "RE" (amount received
    in the account)

    Args:
        transaction_type (str): Transaction type set by the client
        credit_account (str): Credit account set by the client

    Returns:
        bool: Returns False if the transaction_type set is one of the possible
        credit transactions and the client didn't set a value in the credit_account
        field
    """

    credit_transaction_types = ['TI', 'DE', 'RE']

    if (not credit_account) and (transaction_type in credit_transaction_types):
        return False
    else:
        return True


def not_credit_transactions_validation(
    transaction_type: str, credit_account: str
) -> bool:
    """Checks if the client set a credit account if the transaction type was not
    one of the possible credit transactions: "TI" (transfer between accounts from
    the same bank), "DE" (deposit), "RE" (amount received in the account), and
    also if they didn't set one if the transaction type was not one of these

    Args:
        transaction_type (str): Transaction type set by the client
        credit_account (str): Credit account set by the client

    Returns:
        bool: Returns False if the transaction_type set is not one of the possible
        credit transactions and the client has set a value in the credit_account
        field
    """

    credit_transaction_types = ['TI', 'DE', 'RE']

    if (credit_account) and not (transaction_type in credit_transaction_types):
        return False
    else:
        return True
