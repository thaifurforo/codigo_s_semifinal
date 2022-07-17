"""Module that contains the validators for the active_account field from the Customer serializer.
"""


from virtual_bank.utilities import create_check_digit_module_11


def document_number_numeric_validate(document_number: str) -> bool:
    """Checks if the document number set by the client is numeric only

    Args:
        document_number (str): Document number set by the client

    Returns:
        bool: Returns True if the document_number is numeric only
    """
    return document_number.isnumeric()


def cnpj_check_digit_validate(document_number: str) -> bool:
    """Checks if the check digit from the document number field, if it is a CNPJ,
    is valid, according to the standard equation established by the Special
    Department of Federal Revenue of Brazil

    Args:
        document_number (str): Document number set by the client

    Returns:
        bool: Returns True if the check digit of the document_number is valid
    """

    document_number_no_dv = document_number[0:-2]
    weights = [9, 8, 7, 6, 5, 4, 3, 2]
    dv1 = create_check_digit_module_11(document_number_no_dv, weights, reverse=True)
    document_number_dv1 = str(document_number_no_dv) + str(dv1)
    dv2 = create_check_digit_module_11(document_number_dv1, weights, reverse=True)
    cpf_cnpj_dv = str(document_number_dv1) + str(dv2)
    return cpf_cnpj_dv == document_number


def cnpj_length_validate(document_number: str) -> bool:
    """Checks if the the document number field, if it is a CNPJ, is 14 digits long,
    according to the standard format established by the Special Department of
    Federal Revenue of Brazil

    Args:
        document_number (str): Document number set by the client

    Returns:
        bool: Returns True if the length of the document_number is valid"""

    return len(str(document_number)) == 14


def cpf_check_digit_validate(document_number: str) -> bool:
    """Checks if the check digit from the document number field, if it is a CPF,
    is valid, according to the standard equation established by the Special
    Department of Federal Revenue of Brazil

    Args:
        document_number (str): Document number set by the client

    Returns:
        bool: Returns True if the check digit of the document_number is valid
    """

    document_number_no_dv = document_number[0:-2]
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    dv1 = create_check_digit_module_11(document_number_no_dv, weights)
    document_number_dv1 = str(document_number_no_dv) + str(dv1)
    weights = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    dv2 = create_check_digit_module_11(document_number_dv1, weights)
    document_number_dv = str(document_number_dv1) + str(dv2)
    return document_number_dv == document_number


def cpf_length_validate(document_number: str) -> bool:
    """Checks if the the document number field, if it is a CPF, is 11 digits long,
    according to the standard format established by the Special Department of
    Federal Revenue of Brazil

    Args:
        document_number (str): Document number set by the client

    Returns:
        bool: Returns True if the length of the document_number is valid"""

    return len(str(document_number)) == 11
