n = int(input())

for i in range(0,n):

    x, y, z = map(float, input().split())
    m = (2 * x + 3 * y + 5 * z)/10

    print(f'{m:.1f}')