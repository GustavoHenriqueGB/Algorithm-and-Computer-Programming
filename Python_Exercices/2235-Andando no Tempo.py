a, b, c = map(int, input().split())

if a == b or c == b or a == c or a == b+c or b == a+c or c == b+a:
    print('S')
else:
    print('N') 