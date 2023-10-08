A, B, C, D = map(int, input().split())
if B>C and D>A and 0<C+D>A+B>0 and A%2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')