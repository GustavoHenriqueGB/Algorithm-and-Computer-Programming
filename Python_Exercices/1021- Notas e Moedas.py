num, real = map(int, input().split('.'))
n100 = int(num // 100)
n50 = int(num % 100 // 50)
n20 = int(num % 100 % 50 // 20)
n10 = int(num % 100 % 50 % 20 // 10)
n5 = int(num % 100 % 50 % 20 % 10 // 5)
n2 = int(num % 100 % 50 % 20 % 10 % 5 // 2)
m1 = int(num % 100 % 50 % 20 % 10 % 5 % 2 // 1)
m50 = int(round(real // 50))
m25 = int(round(real % 50 // 25))
m10= int(round(real % 50 % 25 // 10))
m5 = int(round(real % 50 % 25 % 10 // 5))
m01 = int(round(real % 5 // 1))
print(f'''NOTAS:
{n100} nota(s) de R$ 100.00
{n50} nota(s) de R$ 50.00
{n20} nota(s) de R$ 20.00
{n10} nota(s) de R$ 10.00
{n5} nota(s) de R$ 5.00
{n2} nota(s) de R$ 2.00
MOEDAS:
{m1} moeda(s) de R$ 1.00
{m50} moeda(s) de R$ 0.50
{m25} moeda(s) de R$ 0.25
{m10} moeda(s) de R$ 0.10
{m5} moeda(s) de R$ 0.05
{m01} moeda(s) de R$ 0.01''')
