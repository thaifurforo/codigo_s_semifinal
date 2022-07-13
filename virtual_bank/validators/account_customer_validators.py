def change_customer(update_customer, current_customer):
    """Returns true if the client tries to set a update to the customer field in
    the account object after it's already created"""
    return update_customer != current_customer
