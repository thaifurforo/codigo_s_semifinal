def transaction_date_most_recent_than_account_opening_date(transaction_date, account_opening_date):
    return transaction_date > account_opening_date


def transaction_in_active_account(account_active):
    return account_active
