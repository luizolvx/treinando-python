print('=== ex040 Media nota ===')

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua Segunda nota: '))
media = (nota1 + nota2) / 2

if media < 4.9:
    print('REPROVADO!!')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO!!')
else:
    print('APROVADO!!')


