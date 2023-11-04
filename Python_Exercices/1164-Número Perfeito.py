n = int(input())

for i in range(0,n):
    x = int(input())
    c = 0

    for j in range(1,x):

        if x % j == 0:
            c += j
            
    if x == c:
        print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')