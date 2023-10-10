h1, h2= map(int, input().split())

hf = h2 * 60 - h1 *60

if hf <= 0:
    hf += 24*60

print(f'O JOGO DUROU {hf//60} HORA(S)')
    
