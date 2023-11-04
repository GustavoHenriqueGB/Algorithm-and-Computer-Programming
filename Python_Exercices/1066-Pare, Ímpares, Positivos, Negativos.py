pa = im = po = ne = 0

for i in range(0,5):

    x = int(input())

    if x != 0:
        if x > 0:
            po += 1
        else:
            ne += 1 

    if x % 2 ==  0:
        pa += 1 
    else:
        im += 1
    
print(f'''{pa} valor(es) par(es)
{im} valor(es) impar(es)
{po} valor(es) positivo(s)
{ne} valor(es) negativo(s)''')