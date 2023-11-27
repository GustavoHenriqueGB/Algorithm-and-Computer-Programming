x = input()
y = int(x)
count = 0

while y > 0:
    for i in x:
        count += 1 
    y -= 1
    x = str(y) 

print(count)