x = int(input())
n = 0

while x != 0:

    d=0
    n += 1
    print(f'Teste {n}')

    for i in range(0, x):
        a, b = map(int, input().split())
        d += a - b
        print(d)
    print('')

    x = int(input())