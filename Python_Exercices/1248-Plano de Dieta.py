n = int(input())

while n > 0:
    dieta = input()
    cafe = input()
    almoco = input()
    comidos = almoco + cafe

    for comida in range(len(comidos)):

        if comidos[comida] not in dieta:
            dieta = 'CHEATER'
            break
        else:
            dieta = dieta.replace(comidos[comida], '')

    if dieta != 'CHEATER':
        dieta = ''.join(sorted(dieta))

    print(dieta)

    n -= 1