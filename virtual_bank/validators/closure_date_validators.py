# from rest_framework import serializers


def closure_date_greater_than_opening_date_validate(closure_date, opening_date) -> bool:
    '''Só poderá haver data de encerramento se a conta estiver marcacda como inativa'''
    if closure_date:
        return closure_date > opening_date
    else:
        return True


# def closure_date_bigger_than_last_transaction_date(closure_date, account_number: str) -> bool:

#     transactions_credit = serializers.ReadOnlyField(
#         source='transaction.credit_account').order_by('date')
#     transactions_debit = serializers.ReadOnlyField(
#         source='transaction.debit_account').order_by('date')

#     return transactions_credit[0]['date'] <= closure_date and transactions_debit[0]['date'] <= closure_date
