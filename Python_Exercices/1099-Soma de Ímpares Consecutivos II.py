n = int(input())

for i in range(0,n):
    lista = list(map(int, input().split()))
    lista.sort()
    x = lista[1]
    y = lista[0]
    soma = 0

    while x > y:
        if x % 2 == 0:
            x - 1 
            soma += x
        else:
            x - 2
            soma += x
    print(soma)