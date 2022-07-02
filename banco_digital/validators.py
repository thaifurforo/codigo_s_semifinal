import re

def dv_modulo_11(numero: str, pesos: list, reverse: bool = False):
  divisao_multiplicadores_numero = int(1 if len(numero) == len(pesos) else round((len(numero) / len(pesos)) + 0.5, 0))
  calculo_verificador = 0
  if reverse:
    pesos_reverse = pesos[:]
    pesos_reverse.reverse()
    lista_multiplicadores = pesos_reverse * divisao_multiplicadores_numero
    i = -1
    while i >= - len(numero):
      calculo_verificador += int(numero[i]) * lista_multiplicadores[i]
      i -= 1
  else:
    lista_multiplicadores = pesos * divisao_multiplicadores_numero
    i = 0
    while i <= len(numero) - 1:
      calculo_verificador += int(numero[i]) * lista_multiplicadores[i]
      i += 1
  calculo_verificador = calculo_verificador * 10 % 11
  dv = calculo_verificador if float(calculo_verificador).is_integer() else round(calculo_verificador + 0.5)
  # dv = 11 - dv
  if dv >= 10 or dv <= 1:
    dv = 0
  return dv

def cpf_cnpj_tamanho_valido(cpf_cnpj, tipo):
  """Verifica se o campo tem 11 caracteres, no caso de CPF, ou 14 caracteres, no caso de CNPJ"""
  if tipo == 'PF':
    return len(str(cpf_cnpj)) == 11
  if tipo == 'PJ':
    return len(str(cpf_cnpj)) == 14

def cpf_cnpj_digito_verificador_valido(cpf_cnpj, tipo):

  if tipo == 'PF':
    cpf_cnpj_sem_dv = cpf_cnpj[0:-2]
    pesos = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    dv1 = dv_modulo_11(cpf_cnpj_sem_dv, pesos)
    cpf_cnpj_dv1 = str(cpf_cnpj_sem_dv)+str(dv1)
    pesos = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    dv2 = dv_modulo_11(cpf_cnpj_dv1, pesos)
    cpf_cnpj_dv = str(cpf_cnpj_dv1)+str(dv2)
    return cpf_cnpj_dv == cpf_cnpj

  if tipo == 'PJ':
    cpf_cnpj_sem_dv = cpf_cnpj[0:-2]
    pesos = [2, 3, 4, 5, 6, 7, 8, 9]
    dv1 = dv_modulo_11(cpf_cnpj_sem_dv, pesos, reverse=True)
    cpf_cnpj_dv1 = str(cpf_cnpj_sem_dv)+str(dv1)
    dv2 = dv_modulo_11(cpf_cnpj_dv1, pesos, reverse=True)
    cpf_cnpj_dv = str(cpf_cnpj_dv1)+str(dv2)
    return cpf_cnpj_dv == cpf_cnpj
    
# def telefone_valido(telefone):
#   """Verifica se o telefone está em um dos formatos aceitos
#   Fixo: +DI (DDD) 0000-0000
#   Celular: +DI (DDD) 00000-0000"""
#   modelo = '+[0-9]{2} \(0[0-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}-[0-9]{4}'
#   resposta = re.findall(modelo, telefone)
#   return resposta