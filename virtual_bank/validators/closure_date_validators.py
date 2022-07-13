def closure_date_greater_than_opening_date_validate(closure_date, opening_date) -> bool:
    '''Só poderá haver data de encerramento se a conta estiver marcacda como inativa'''
    if closure_date:
        return closure_date > opening_date
    else:
        return True


def closure_date_most_recent_than_last_transaction_date(last_credit_transaction_date, last_debit_transaction_date, closure_date) -> bool:

    if last_debit_transaction_date:
        closure_date_most_recent_than_last_debit = last_debit_transaction_date <= closure_date
    else:
        closure_date_most_recent_than_last_debit = True

    if last_credit_transaction_date:
        closure_date_most_recent_than_last_credit = last_credit_transaction_date <= closure_date
    else:
        closure_date_most_recent_than_last_credit = True

    return closure_date_most_recent_than_last_debit and closure_date_most_recent_than_last_credit
