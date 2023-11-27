V, N = map(int, input().split())

vtotal = V * N
placa = 0
i = 10

while i < 90:
    placa = vtotal // i
    if vtotal % i != 0:
        placa += 1 
    print(placa, end=' ')
    i += 10

placa = vtotal // 90
if vtotal % 90 != 0:
    placa += 1 
print(placa)