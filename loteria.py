from random import randint
print('=== ex 091 ===')

apostas = list()
jogador = dict()

for j in range(3):
    print('\n','=-'*4, '-<| CADASTRO JOGADOR |>-', '=-'*4)
    jogador['nome'] = str(input('Nome: '))
    jogador['numero_sorteado'] = int(randint(1, 100))
    print(f'Nº sorteado: {jogador["numero_sorteado"]}')
    apostas.append(jogador.copy())

print('\nResultados do sorteio:')
for j in apostas:
    print(f"{j['nome']} - Número Sorteado: {j['numero_sorteado']}")

maior_numero = -1
for j in apostas:
    if j['numero_sorteado'] > maior_numero:
        maior_numero = j['numero_sorteado']
        ganhador = j
print(f"\n O ganhador é {ganhador['nome']} com o número {ganhador['numero_sorteado']}!")

