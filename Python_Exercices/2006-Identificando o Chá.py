cha = int(input())
count = 0 
a, b, c, d, e = map(int, input().split())

if cha == a:
    count += 1
if cha == b:
    count += 1
if cha == c:
    count += 1
if cha == d:
    count += 1
if cha == e:
    count += 1

print(count)
