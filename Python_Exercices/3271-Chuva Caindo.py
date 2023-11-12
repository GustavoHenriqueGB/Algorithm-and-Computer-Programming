def bhaskara(a,b,c):
    return(b+(b**2-4*a*c)**(1/2))/(2*a)

def calcular_precipitacao1(L, K, T1, T2, H):
    if L < H:
        return (bhaskara(T1, H + K * (T1 + T2 ), K * L)) * T1
    else:
        return H

def calcular_precipitacao2(L, K, T1, T2, H):
    if L > H:
        return H
    else:
        return (bhaskara(T1, H + K * (T1 + T2 ), K * L)) * T1

L, K, T1, T2, H = map(float, input().split())

ans = calcular_precipitacao1(L, K, T1, T2, H), calcular_precipitacao2(L, K, T1, T2, H)
print(F'{ans[0]:.9F} {ans[1]:.9F}')