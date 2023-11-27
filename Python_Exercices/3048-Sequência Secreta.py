n = int(input())
count = aux = 0

for i in range(0, n):
    x = int(input())

    if i == 0:  
        count += 1
        aux = x
    else:
        if x != aux:
            count += 1
            aux = x

print(count)