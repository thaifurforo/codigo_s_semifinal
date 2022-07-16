"""Module that contains the validators for the customer field from the Account serializer.
"""


def change_customer(update_customer, current_customer) -> bool:
    """Checks if the client is trying to set an update to the customer field
    in the account object after it's already created

    Args:
        update_customer (Customer): The customer field set in the update request (PUT or PATCH)
        current_customer (Customer): The customer field saved in the object instance

    Returns:
        bool: Returns True if the update_customer is different from the current_customer"""

    return update_customer != current_customer
