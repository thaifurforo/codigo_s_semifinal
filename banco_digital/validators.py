from configparser import ConfigParser
from typing import Union

def check_digit_module_11(number: Union[str, int], weights: list, reverse: bool = False):
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

def cpf_cnpj_tamanho_valido(cpf_cnpj: Union[str, int], tipo: str):
  """Verifica se o campo tem 11 caracteres, no caso de CPF, ou 14 caracteres, no caso de CNPJ"""
  try:
    cpf_cnpj = str(cpf_cnpj)
  except:
    raise TypeError('O parâmetro "cpf_cnpj" deve ser um integer ou uma string com somente números')
  if tipo == 'PF':
    return len(str(cpf_cnpj)) == 11
  if tipo == 'PJ':
    return len(str(cpf_cnpj)) == 14

def cpf_cnpj_digito_verificador_valido(cpf_cnpj: Union[str, int], tipo: str):
  try:
    cpf_cnpj = str(cpf_cnpj)
  except:
    raise TypeError('O parâmetro "cpf_cnpj" deve ser um integer ou uma string com somente números')
  if tipo == 'PF':
    cpf_cnpj_sem_dv = cpf_cnpj[0:-2]
    pesos = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    dv1 = check_digit_module_11(cpf_cnpj_sem_dv, pesos)
    cpf_cnpj_dv1 = str(cpf_cnpj_sem_dv)+str(dv1)
    pesos = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    dv2 = check_digit_module_11(cpf_cnpj_dv1, pesos)
    cpf_cnpj_dv = str(cpf_cnpj_dv1)+str(dv2)
    return cpf_cnpj_dv == cpf_cnpj

  if tipo == 'PJ':
    cpf_cnpj_sem_dv = cpf_cnpj[0:-2]
    pesos = [2, 3, 4, 5, 6, 7, 8, 9]
    dv1 = check_digit_module_11(cpf_cnpj_sem_dv, pesos, reverse=True)
    cpf_cnpj_dv1 = str(cpf_cnpj_sem_dv)+str(dv1)
    dv2 = check_digit_module_11(cpf_cnpj_dv1, pesos, reverse=True)
    cpf_cnpj_dv = str(cpf_cnpj_dv1)+str(dv2)
    return cpf_cnpj_dv == cpf_cnpj