lista = []
count = 0

for i in range(10):
    lista.append(int(input()))

for i in lista:

    if i > 0:
        print(f'X[{count}] = {i}')
        
    else:
        print(f'X[{count}] = {1}')
    
    count += 1