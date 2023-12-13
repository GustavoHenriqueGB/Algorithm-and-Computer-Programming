def soma(matriz, l, t):
    soma = 0
    
    for i in range(len(matriz)):
        if i == l:
            for j in matriz[i]:
                soma += j
    
    if t == 'S':
        print(soma)
    elif t == 'M':
        print(soma/12)

l = int(input())
t = input()

matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)
    
soma(matriz, l, t)

        
