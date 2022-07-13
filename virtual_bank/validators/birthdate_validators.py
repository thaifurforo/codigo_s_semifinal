def birthdate_not_null(birthdate) -> bool:
    """Checks if the birthdate is not a null value - which it shouldn't be if
    the customer is a natural person (PF) and should be if the customer is a
    juridical person (PJ)

    Args:
        birthdate (date): Birthdate informed by the client

    Returns:
        bool: Returns True if the client informed a birthdate
    """
    return birthdate != None
