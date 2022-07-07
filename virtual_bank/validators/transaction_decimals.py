def transaction_decimals_validate(amount: float) -> bool:
  return round(amount, 2) == amount