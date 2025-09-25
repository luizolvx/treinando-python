from random import randint
from time import sleep

print('=== ex 088 ===')


lista_geral = []
temp = []
cont = 0

quant = int(input('Quantos jogos você quer que eu sorteie? '))

print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)

while cont < quant:
    c = 0
    while True:
        num = randint(1, 60)
        if num not in temp:
            temp.append(num)
            c += 1
        if c >= 6:
            break

    temp.sort()
    lista_geral.append(temp[:])
    temp.clear()

    sleep(0.5)
    print(f'Jogo {cont + 1}: {lista_geral[cont]}')

    cont += 1

print('-=' * 5, ' BOA SORTE! ', '-=' * 5)