n = int(input())
c = r = s = t = 0

for i in range(0,n):

  q,a = input().split()
  q = int(q)
  t += q

  if a == 'C':
    c += q
  elif a == 'R':
    r += q
  elif a == 'S':
    s += q 

print(f'''Total: {t} cobaias
Total de coelhos: {c}
Total de ratos: {r}
Total de sapos: {s}
Percentual de coelhos: {100*c/t:.2f} %
Percentual de ratos: {100*r/t:.2f} %
Percentual de sapos: {100*s/t:.2f} %''')