def verificador(compactado):

    descompactado = ""
    um = False
    digito = 0

    for i in compactado:

        if um:
            descompactado += '1' * int(i)
            um = False

        else:
            descompactado += '0' * int(i)
            um = True

    qtdum = descompactado.count('1')
    qtdzero = descompactado.count('0')
    
    for _ in str(qtdzero):
        digito += int(_)

    for _ in str(qtdum):
        digito += int(_)
    
    return digito


n = int(input())

while n != 0:
    
    while n > 0:
        
        compactado = input()
        digito = verificador(compactado)
        print(digito)
        
        n -= 1
        
    n = int(input())

