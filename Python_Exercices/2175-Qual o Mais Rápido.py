def min(x,y,z):

    if  x < y and x < z:
        print('Otavio')
    elif  z < y and z < x:
        print('Ian')
    elif  y < x and y < z:
        print('Bruno')
    elif x == y or y == z or x == z:
        print('Empate')

o, b, i = map(float, input().split())
min(o,b,i)

