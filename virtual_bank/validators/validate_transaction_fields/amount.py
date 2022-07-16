"""Module that contains the validators for the amount field from the Transaction serializer.
"""


def transaction_decimals_validate(amount: float) -> bool:
    """Checks if the transaction amount set by the client has a maximum of 2 decimal
    places

    Args:
        amount (float): Amount set by the client

    Returns:
        bool: Returns true if the amount field has a maximum of 2 decimal places
    """
    return round(amount, 2) == amount
