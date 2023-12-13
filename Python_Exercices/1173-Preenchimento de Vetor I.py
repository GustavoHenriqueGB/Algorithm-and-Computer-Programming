v = int(input())

for i in range(10):

    if i == 0:
       print(f'N[{i}] = {v}')

    else:
        print(f'N[{i}] = {v * 2}')
        v *= 2