lista = []
lista.append(int(input()))
lista.append(int(input()))
lista.sort()

x = lista[1]
y = lista[0]
soma = 0


for i in range(y, x + 1):
    if i % 13 != 0:
        soma += i


print(soma)