def change_opening_date(update_opening_date, current_opening_date):
        """Returns true if the client tries to set a update to the opening_date
        field in the account object after it's already created"""
        return update_opening_date != current_opening_date
