from random import randint
print('===ex 058 ===')

chute = int(input('Tente adivinhar o número sorteado: '))

sorteado = randint(0,10)
contador = 1
while chute != sorteado:
    print('VOCÊ ERROU, TENTE NOVAMENTE!')
    chute = int(input('Adivnhe o número sorteado: \n'))
    contador += 1
if chute == sorteado:
    print("\nNúmero Sorteado: {}".format(sorteado))
    print('PARABÉNS VOCÊ ACERTOU!!!')
    print('Tentativas: {}'.format(contador))