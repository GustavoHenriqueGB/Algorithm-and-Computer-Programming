c, q = map(int, input().split())
if c == 1:
    print(f'Total: R$ {q * 4.00:.2f}')
elif c == 2:
    print(f'Total: R$ {q * 4.50:.2f}')
elif c == 3:
    print(f'Total: R$ {q * 5.00:.2f}')
elif c == 4:
    print(f'Total: R$ {q * 2.00:.2f}')
elif c == 5:
    print(f'Total: R$ {q * 1.50:.2f}')