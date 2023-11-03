def par(a):

    if a <= 100:
        print(a)
        a += 2
        par(a)
        
par(2) 