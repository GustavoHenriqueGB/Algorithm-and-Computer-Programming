x , y = map(int, input().split())

for i in range(1, y + 1, x):

    for j in range(0,x):

        if j != x - 1:
            print(i, end=' ')
            i += 1
        else:
            print(i)
            i += 1
