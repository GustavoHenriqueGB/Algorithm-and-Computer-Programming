def lingua(lista):
    
    count = 0
    aux = ''

    for i in lista:
        if count == 0:
            aux = i
            count += 1

        else:
            if i != aux:
                return 'ingles'
            
    return aux

            
n = int(input())

for _ in range(n):

    x = int(input())
    lista = []
    
    for _ in range(x):

        lista.append(input())

    idioma = lingua(lista)
        
    print(idioma)
        
