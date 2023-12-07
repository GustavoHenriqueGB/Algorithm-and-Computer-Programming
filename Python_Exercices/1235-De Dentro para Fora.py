def corretor(x):
    
    string_nova =''
    string_nova += string[len(string)//2-1::-1]
    string_nova += string[len(string):len(string)//2-1:-1]
    print(string_nova)
    
n = int(input())

while n != 0:
    string = input()
    corretor(string)
    n -= 1



