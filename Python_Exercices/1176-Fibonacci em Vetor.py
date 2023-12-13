def fibonacci(lista, a, b,):
    
    fibonacci_lista = [0, 1]
    aux = 0
    count = 1

    while count <= max(lista):

        aux = a + b
        a = b
        b = aux

        fibonacci_lista.append(aux)

    for i in lista:
        fibonacci_lista.index(i)
        print(f'Fib({})')

t = int(input())
lista = []

for i in range(t):
    lista.append(int(input()))

lista_correta = fibonacci(lista, 0, 1)

for i in lista_correta:
