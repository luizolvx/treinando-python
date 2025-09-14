print('=== ex 064 ===')

soma = 0
contagem = 0

print('Digite vários números inteiros. O programa para quando você digitar 999.')

while True:
    numero = int(input('Digite um número (ou 999 para parar): '))
    if numero == 999:
        break
    soma += numero
    contagem += 1

print('---')
print('Você digitou {} números, e a soma entre eles é {}.'.format(contagem, soma))