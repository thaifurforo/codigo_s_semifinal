def debit_transactions_validation(transaction_type, debit_account):
    if (not debit_account) and ((transaction_type == 'TI') or (transaction_type == 'TE') or (transaction_type == 'PG') or (transaction_type == 'SQ')):
        return False
    else:
        return True


def credit_transactions_validation(transaction_type, credit_account):
    if (not credit_account) and ((transaction_type == 'TI') or (transaction_type == 'DE') or (transaction_type == 'RE')):
        return False
    else:
        return True


def not_debit_transactions_validation(transaction_type, debit_account):
    if (debit_account) and ((transaction_type == 'DE') or (transaction_type == 'RE')):
        return False
    else:
        return True


def not_credit_transactions_validation(transaction_type, credit_account):
    if (credit_account) and ((transaction_type == 'TE') or (transaction_type == 'PG') or (transaction_type == 'SQ')):
        return False
    else:
        return True
