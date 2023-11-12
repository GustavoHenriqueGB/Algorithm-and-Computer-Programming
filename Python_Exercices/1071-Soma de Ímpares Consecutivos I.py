import sys
sys.setrecursionlimit(100000)

def pa(a,b):
    if a > b:
        return 0
    elif a % 2 != 0:
        return a + pa(a + 2, b)
    else:
        return pa(a + 1,b)

lista = []
lista.append(int(input()))
lista.append(int(input()))
lista = sorted(lista)

x = lista[0]
y = lista[1]

ans = pa(x + 1,y - 1)
print(ans)