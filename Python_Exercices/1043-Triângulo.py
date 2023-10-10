a, b, c = map(float, input().split())
if b+c > a > abs(b-c) or a+c > b > abs(a-c) or b+a > c > abs(b-a):
    print(f'Perimetro = {a+b+c:.1f}')
else:
    print(f'Area = {(a + b)* c / 2:.1f}')