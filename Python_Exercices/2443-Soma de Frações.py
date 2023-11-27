def mdc(a, b):
    if b == 0:
        return a
    else:    
        return mdc(b, a % b)

a, b, c, d = map(int, input().split())
dividendo = divisor = 0

if b == d:
    dividendo = a + c 
    divisor = b
else:
    divisor = b * d
    dividendo = (divisor / b * a ) + (divisor / d * c)

gcd = mdc(dividendo, divisor)
dividendo = dividendo // gcd
divisor = divisor // gcd

print(f'{dividendo:.0f} {divisor:.0f}')