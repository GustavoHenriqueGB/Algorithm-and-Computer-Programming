def tamanho(nomes):
    maior = 0

    for nome in nomes:

        if len(nome) > maior:
            maior = len(nome)

    return maior 

count = 0
n = int(input())

while n != 0:
    nomes = []

    while n > 0:
        nomes.append(input())
        n -= 1

    maior = tamanho(nomes)
    for nome in nomes:
        print((maior - len(nome)) * ' '+nome)
    
    n = int(input())
    if n != 0:
        print()