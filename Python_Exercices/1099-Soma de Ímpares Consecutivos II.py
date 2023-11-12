
n = int(input())

for i in range(0,n):
    lista = list(map(int, input().split()))
    lista.sort()
    x = lista[1]
    y = lista[0]
    soma = 0

    if x == y:
        print(0)

    else:
        while x > y:
            if x % 2 == 0:
                soma += x
                x -= 1 
            
            else:
                soma += x
                x -= 2
                
        print(soma - lista[1])