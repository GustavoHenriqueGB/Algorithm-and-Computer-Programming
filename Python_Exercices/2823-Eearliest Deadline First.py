n = int(input())
soma = 0

for i in range(0,n):
    x1, x2 = map(float, input().split())
    soma += x1 / x2

if soma <= 1.0:
    print('OK')
else:
    print('FAIL')