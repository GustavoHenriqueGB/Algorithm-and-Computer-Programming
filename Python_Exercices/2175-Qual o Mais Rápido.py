def min(x,y):

    if x < y:
        return(x)
    elif x == y:
        print('Empate')
    else:
        return(y)

o, b, i = map(float, input().split())
mr = min(min(o,b), i)
mr = float(mr)
if mr == o:
    print('Otavio')
elif mr == b:
    print('Bruno')
elif mr == i:
    print('Ian')
