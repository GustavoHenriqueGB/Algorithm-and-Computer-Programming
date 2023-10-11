p, r = map(int, input().split())

if p == 0:
    print('C')
elif p == 1:
    if r == 0:
        print('B')
    elif r == 1:
        print('A')
