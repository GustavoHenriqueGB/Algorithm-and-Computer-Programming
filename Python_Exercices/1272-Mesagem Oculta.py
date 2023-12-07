def corretor(x):
    
    string_nova =''
    lista = list(map(str, x.split()))
    for i in lista:
        string_nova += i[0]
    print(string_nova)
    
n = int(input())

while n != 0:
    string = input().strip()
    corretor(string)
    n -= 1
