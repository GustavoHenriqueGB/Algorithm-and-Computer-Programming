c = g = a = d = 0

while c != 4:
    c = int(input())

    if c == 1:
        a += 1
    elif c == 2:
        g += 1 
    elif c == 3:
        d += 1

print(f'''MUITO OBRIGADO
Alcool: {a}
Gasolina: {g}
Diesel: {d}''')