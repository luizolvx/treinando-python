import os
from random import randint
print('=== ex 068 ===\n')

while True:
    print('\t--- Painel de Escolha ---')
    print('[1] PAR')
    print('[2] IMPAR')

    opcao = int(input('Escolha [1]Par ou [2]Impar: '))
    numero_adversario = randint(1, 10)

    if opcao == 1:
        print('VOCÊ ESCOLHEU PAR')
        numero = int(input('Agora digite um numero de 1 a 10: '))
        if numero > 10 or numero < 1:
            print('Você deve Digitar um numero de 1 a 10')
            break
        elif (numero + numero_adversario) % 2 == 0:
            print('PARABÉNSSS VOCÊ GANHOU!!!')
        else:
            print('VOCÊ PERDEU!!!')
            break
    elif opcao == 2:
        print('VOCÊ ESCOLHEU IMPAR')
        numero = int(input('Agora digite um numero de 1 a 10: '))
        if numero > 10 or numero < 1:
            print('Você deve Digitar um numero de 1 a 10')
            break
        elif (numero + numero_adversario) % 2 != 0:
            print('PARABÉNSSS VOCÊ GANHOU!!!')
        else:
            print('VOCÊ PERDEU!!!')
            break
    elif opcao != 1 or 2:
        print('Você deve escolher umas das opções válidas')
        break

    input('\nPressione ENTER para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')