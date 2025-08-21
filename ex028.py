print('=== 028 ===')
from random import randint
numero_aleatorio = randint(0, 5)
numero_tentativa = int(input('Digite um Número entre 0 e 5: '))
if numero_tentativa > 5 or numero_tentativa < 0:
    print('Tentativa invalida! Digite um Número entre 0 e 5')
else:
    if numero_aleatorio == numero_tentativa:
        print('PARABÉÉÉNSSS, Você Acertou o número SORTEADO')
    else:
        print('QUE PENA! Você errou o número SORTEADO')
    print('O Número sorteado foi o {}' .format(numero_aleatorio))