print('=== ex 065 ===')

soma = 0
contagem = 0
maior = 0
menor = 0
continuar = 'S'

while continuar in 'Ss':
    numero = int(input('Digite um número inteiro: '))

    if contagem == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    soma += numero
    contagem += 1

    continuar = str(input('Quer continuar [S/N]? ')).strip().upper()

if contagem > 0:
    media = soma / contagem
    print('---')
    print('Você digitou {} números.'.format(contagem))
    print('A média dos valores digitados foi {:.2f}.'.format(media))
    print('O maior valor digitado foi {}.'.format(maior))
    print('O menor valor digitado foi {}.'.format(menor))
else:
    print('---')
    print('Nenhum número foi digitado.')