def pa(a,b,c):
    if a % 2 == 0:
        a -= 1
        pa(a,b,c)
    else:
        for i in range(a,b,-2):
            c += i
    print(c)
lista = []
lista.append(int(input()))
lista.append(int(input()))
sorted(lista)

x = lista[0]
y = lista[1]
z = 0

if x == y:
    print(0)

else:
    if y % 2 == 0:
        y += 1
    else:
        y += 2 
    pa(x,y,z)