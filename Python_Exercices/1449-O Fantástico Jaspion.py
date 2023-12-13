t = int(input())

while t > 0:
    dicionario = {}
    m, n = map(int, input().split())
    
    while m * 2 > 0:
        aux = input()
        dicionario [aux] = input()
        m -= 1
        
    while n > 0:
        escreva = ''
        lista = list(map(str, input().split()))
        
        for i in lista:
            
            if i in dicionario.keys():
                escreva += dicionario[i]
                escreva += ' '
                
            else:
                escreva += i
                escreva += ' '
            
        print(escreva.strip())
        
            
        n -= 1
        
    print()
    t -= 1 


