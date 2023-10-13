n1, n2 , n3, n4 = map(float, input().split())
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10

print(f'Media: {media:.1f}')

if media >= 7.0:
    print('Aluno aprovado.')

elif media < 5.0:
    print('Aluno reprovado.')

elif 5.0 <= media <= 6.9:
    print('Aluno em exame.')
    exame = float(input())
    media = (exame + media) / 2 

    if media >= 5.0:
        print(f'Nota do exame: {exame:.1f}')
        print('Aluno aprovado.')
        print(f'Media final: {media:.1f}')
        
    else:
        print(f'Nota do exame: {exame:.1f}')
        print('Aluno reprovado.')
        print(f'Media final: {media:.1f}')
