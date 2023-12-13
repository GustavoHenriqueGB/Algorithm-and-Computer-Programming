def aspas(texto, i):

  count = 0
  count2 = 0
  aspas = []
  ignorar = False
  lista_ignorar = []


  for _ in texto:
      if _ == '"':
          aspas.append(count)

      count += 1

  qtdaspas = len(aspas)

  for _ in texto:
      lista_ignorar.append(ignorar)

      if _ == '"':

          if ignorar == False and qtdaspas % 2 == 0:
              ignorar = True

          elif ignorar == False and qtdaspas % 2 != 0 and count2 == max(aspas):
              pass

          elif ignorar == False and qtdaspas % 2 != 0 and count2 != max(aspas):
              ignorar = True

          elif ignorar == True and qtdaspas % 2 != 0 and count2 != max(aspas):
              ignorar = False

          elif ignorar == True and qtdaspas % 2 == 0:
              ignorar = False

      count2 += 1

  return lista_ignorar[i]




def espacos(texto):
  count = 0
  qtdespacos = []

  for _ in range(0, len(texto) - 1):
      if aspas(texto, count):
           pass

      else:
          if texto[_] == ' ' and texto[_ + 1] == ' ':
              qtdespacos.append(count + 1)

      count += 1
  return qtdespacos


def numeros(texto):
  count = 0
  qtdnumeros = []

  for _ in range(0, len(texto) - 1):
      if aspas(texto, count):
           pass

      else:
          if texto[_].isalpha() and not texto[_ + 1].isalpha():
              if texto[_ + 1].isdigit():
                  indice = _ + 1

                  while True:
                      try:
                          if indice < len(texto) and texto[indice].isdigit():
                              qtdnumeros.append(indice)
                              indice += 1

                          else:
                              break

                      except texto[indice].isdigit() == False:
                          break

      count += 1
  return qtdnumeros



def upper(texto):
  count = 0
  qtdmaiuscula = []

  for _ in range(len(texto)):
      if aspas(texto, count):
          pass

      else:
          if texto[_].isupper():
              if count == 0 or (_ > 1 and texto[_ - 1] == ' ' and texto[_ - 2] == "."):
                  pass
              else:
                  qtdmaiuscula.append(_)

      count += 1
  return qtdmaiuscula


def lower(texto):
  count = 0
  qtdminuscula = []

  for _ in range(len(texto)):
      if aspas(texto, count):
          pass

      else:
          if texto[_].islower():
              if count == 0 or (_ > 1 and texto[_ - 1] == ' ' and texto[_ - 2] == "."):
                  qtdminuscula.append(_)
              else:
                  pass

      count += 1
  return qtdminuscula


def pontos(texto):
  count = 0
  qtdpontos = []

  for _ in range(0, len(texto) - 1):
      if aspas(texto, count):
           pass

      else:
          if texto[_] in [',', '.', '"'] and (_ < len(texto) and _ > 0 and texto[_ + 1].isalpha() and texto[_ - 1].isalpha()):
              qtdpontos.append(count)

          elif texto[_] in [',', '.', '"'] and texto[_ + 1].isspace() and texto[_ - 1].isspace():
              qtdpontos.append(count)

          else: 
              pass

      count += 1
  return qtdpontos

espacoembranco = []
informal = []
maiuscula = []
minuscula = []
pontuacao = []

texto = input()

espacoembranco = espacos(texto)
informal = numeros(texto)
maiuscula = upper(texto)
minuscula = lower(texto)
pontuacao = pontos(texto)

if len(espacoembranco) != 0 or len(informal) != 0 or len(maiuscula) != 0 or len(minuscula) != 0 or len(pontuacao) != 0:
  print('NAO')

else:
  print('SIM')

if len(espacoembranco) != 0:
  print('ESPACO EM BRANCO')
  print(*espacoembranco)


if len(informal) != 0:
  print('INFORMAL')
  print(*informal)
        

if len(maiuscula) != 0:
  print('MAIUSCULA')
  print(*maiuscula)
        

if len(minuscula) != 0:
  print('MINUSCULA')
  print(*minuscula)
    

if len(pontuacao) != 0:
  print('PONTUACAO')
  print(*pontuacao)

