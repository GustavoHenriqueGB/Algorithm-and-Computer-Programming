x = int(input())

while x != 0:
  
    for i in range(1, x+1):
        if i != x:
            print(i, end=' ')
        else:
            print(i)
            
    x = int(input())