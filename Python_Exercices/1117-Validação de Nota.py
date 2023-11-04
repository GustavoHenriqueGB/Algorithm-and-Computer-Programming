c = m = 0 

while c < 2:
    n = float(input())

    if 0 <= n <= 10:
        m += n
        c += 1 
    else:
        print('nota invalida')

print(f'media = {m/2}')