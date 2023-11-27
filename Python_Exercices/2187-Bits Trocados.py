x = int(input())
n = 0

while x != 0:

    d=0
    n +=1
    cin = x // 50
    dez = x % 50 // 10
    cinco = x % 50 % 10 // 5
    um = x % 50 % 10 % 5 // 1
    
    print(f'Teste {n}')
    print(f'{cin} {dez} {cinco} {um}')
    print()
    x = int(input())
