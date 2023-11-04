p = v =0

for i in range(1,101):

    x = int(input())

    if x > v:
        v = x
        p = i
        
print(v)
print(p)  