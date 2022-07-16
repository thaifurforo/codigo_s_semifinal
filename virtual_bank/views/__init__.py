"""When a regular package is imported, this module is implicitly executed, and
the objects it defines are bound to names in the package’s namespace.
"""

from virtual_bank.views.customer_view import CustomerViewSet
from virtual_bank.views.account_view import AccountViewSet
from virtual_bank.views.transaction_view import TransactionViewSet
from virtual_bank.views.accounts_by_customer_view import AccountsByCustomerView
from virtual_bank.views.transactions_by_account_view import TransactionsByAccountView
