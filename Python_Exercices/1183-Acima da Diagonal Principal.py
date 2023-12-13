def soma(matriz, o):
    soma = 0
    count = 0
    
    for i in range(len(matriz)):
        for j in range(i):
            if j > i:
                soma += i[j]
                count += 1
    
    if o == 'S':
        print(soma)
    elif o == 'M':
        print(soma/count)

o = input()

matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)
    
soma(matriz, o)