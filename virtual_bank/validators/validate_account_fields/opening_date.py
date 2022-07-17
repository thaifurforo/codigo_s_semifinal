"""Module that contains the validators for the opening_date field from the Account serializer.
"""


def change_opening_date(update_opening_date, current_opening_date):
    """Checks if the client is trying to set an update to the opening_date field
    in the account object after it's already created

    Args:
        update_opening_date (datetime.date): The opening_date field set in the update request (PUT or PATCH)
        current_opening_date (datetime.date): The opening_date field saved in the object instance

    Returns:
        bool: Returns True if the update_opening_date is different from the current_opening_date"""

    return update_opening_date != current_opening_date
