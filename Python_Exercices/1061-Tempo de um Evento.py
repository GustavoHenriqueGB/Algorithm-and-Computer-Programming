d1 = int(input().split()[1])
h1, m1 , s1 = map(int, input().split(':'))
d2 = int(input().split()[1])
h2, m2, s2 = map(int, input().split(':'))

s1 = d1 * 24 * 60 * 60 + h1 * 60 * 60 + m1 * 60 + s1
s2 = d2 * 24 * 60 * 60 + h2 * 60 * 60 + m2 * 60 + s2

tempofinal = s2 - s1

if tempofinal <= 0:
    tempofinal += 24 * 60 * 60

print(f'''{tempofinal // 60 // 60 // 24} dia(s)
{tempofinal // 60 // 60 % 24} hora(s)
{tempofinal // 60 % 60} minuto(s)
{tempofinal % 60} segundo(s)''')