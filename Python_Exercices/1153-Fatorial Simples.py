def fatorial(a,b,c):

    if a != 1:
        c = c * a
        b = c
        a -= 1
        fatorial(a,b,c)

    else:
        print(b)

    
x = int(input())
fatorial(x,0,1)