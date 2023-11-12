n = 1 
while n > 0:
        
        lista = list(map(int, input().split()))
        lista.sort()

        soma = 0
        m = lista[1]
        n = lista[0]
        if n > 0:
            while n <= m:
                soma += n 
                print(n, end=' ')
                n += 1

            print(f'Sum={soma}')