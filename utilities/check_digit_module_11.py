from typing import Union

def create_check_digit_module_11(number: Union[str, int], weights: list, reverse: bool = False) -> int:
  """Function to generate a check digit to a number, using the "Module 11" method, widely used in Brazil.
  The method consists in multiplying each digit from the number to the values on the weights' list.
  Then, the results are summed, and the sum result is multiplied by 10 and then divided by 11. 
  The resulting number is rounded up.
  If it is equal or greater than 10, or equal to 0 or 1, the check digit shall be 0.
  Otherwise, this last result is the check digit.

  Args:
      number (int or str): Base number to generate the check digit. 
      weights (list): A list of weights to be multiplied by the digits in the number.
                      If the list is shorter than the number of digits in the number,
                      it will be repeated as many times as required.
      reverse (bool, optional): True to start multiplying the last digits from the number first.
                                Defaults to False.

  Returns:
      int: Returns the check digit, according to the Module 11 method.
  """
  try:
    number = str(number)
  except:
    raise TypeError('O parâmetro "number" deve ser um integer ou uma string com somente números')
  number_divided_multipliers = int(1 if len(number) == len(weights) else round((len(number) / len(weights)) + 0.5, 0))
  check_calculation = 0
  if reverse:
    weights_reverse = weights[:]
    weights_reverse.reverse()
    multipliers_list = weights_reverse * number_divided_multipliers
    i = -1
    while i >= - len(number):
      check_calculation += int(number[i]) * multipliers_list[i]
      i -= 1
  else:
    multipliers_list = weights * number_divided_multipliers
    i = 0
    while i <= len(number) - 1:
      check_calculation += int(number[i]) * multipliers_list[i]
      i += 1
  check_calculation = check_calculation * 10 % 11
  cd = check_calculation if float(check_calculation).is_integer() else round(check_calculation + 0.5)
  # dv = 11 - dv
  if cd >= 10 or cd <= 1:
    cd = 0
  return cd


  