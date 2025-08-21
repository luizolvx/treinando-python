import random

print('=== ex 045 JOKENPO ===')

print('\tOpções de Jogada: ')
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')

jogada = int((input('Selecione a jogada: ')))

jogada_aleatoria = random.randint(1, 3)

if jogada != 1 and jogada != 2 and jogada != 3:
    print('\t\nOpção INVÁLIDA!!')

elif jogada == jogada_aleatoria:
        print('\nEMPATE!')

else:
    if jogada == 1 and jogada_aleatoria == 2:
        print('\nPedra X Papel = PAPEL Ganhou')
        print('Vitória Adversária!')

    elif jogada == 1 and jogada_aleatoria == 3:
        print('- VOCÊ x ADVERSÁRIO -')
        print('Pedra X Tesoura = PEDRA Ganhou')
        print('Parabéns Você Ganhou!')

    elif jogada == 2 and jogada_aleatoria == 1:
        print('- VOCÊ x ADVERSÁRIO -')
        print('Papel X Pedra = PAPEL Ganhou')
        print('Parabéns Você Ganhou!')

    elif jogada == 2 and jogada_aleatoria == 3:
        print('- VOCÊ x ADVERSÁRIO -')
        print('Papel X Tesoura = TESOURA Ganhou')
        print('Vitória Adversária!')

    elif jogada == 3 and jogada_aleatoria == 1:
        print('- VOCÊ x ADVERSÁRIO -')
        print('Tesoura X Pedra = PEDRA Ganhou')
        print('Vitória Adversária!')

    elif jogada == 3 and jogada_aleatoria == 2:
        print('- VOCÊ x ADVERSÁRIO -')
        print('Tesoura X Papel = Tesoura Ganhou')
        print('Parabéns Você Ganhou!')