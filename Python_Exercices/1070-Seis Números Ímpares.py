def impar(a,i):

    if i < 6:
        
        if a % 2 == 0:
            a += 1
            impar(a,i)
        else:
            i += 1
            print(a)
            a += 2
            impar(a,i)
        i += 1

x = int(input())
impar(x, 0) 