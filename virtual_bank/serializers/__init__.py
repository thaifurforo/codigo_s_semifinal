"""When a regular package is imported, this module is implicitly executed, and
the objects it defines are bound to names in the package’s namespace.
"""


from virtual_bank.serializers.account_serializer import AccountSerializer
from virtual_bank.serializers.customer_serializer import CustomerSerializer
from virtual_bank.serializers.transaction_serializer import TransactionSerializer
from virtual_bank.serializers.address_serializer import AddressSerializer
from virtual_bank.serializers.balance_serializer import BalanceSerializer
from virtual_bank.serializers.accounts_by_customer_serializer import (
    AccountsByCustomerSerializer,
)
from virtual_bank.serializers.transactions_by_account_serializer import (
    TransactionsByAccountSerializer,
)
