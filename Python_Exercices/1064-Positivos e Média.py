c = 0
a = 0
for i in range(0,6):

    x = float(input())

    if x > 0:
        c += 1 
        a += x
    
print(f'{c} valores positivos')
print(f'{a/c:.1f}')