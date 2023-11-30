n = int(input())

while n > 0:
    alpha_num = input()
    lista = list(alpha_num)
    x = int(lista[0])
    alpha = lista[1]
    y = int(lista[2])

    if x != y:
        if ord(alpha)  >= 65 and ord(alpha) <= 90:
            print(y - x)

        elif ord(alpha)  >= 97 and ord(alpha) <= 122:
            print(x + y)

    else:
        print(x * y)

    n -= 1