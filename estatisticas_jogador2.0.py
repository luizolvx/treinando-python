print('=== ex 095 - Aproveitamento de Jogadores ===')

time = list()  # Lista principal para armazenar todos os dicionários de jogadores
while True:
    gol_total = 0
    jogador = dict()
    gols = list()


    jogador['nome'] = str(input('Nome: '))
    jogador['partidas'] = int(input('partidas: '))

    for p in range(jogador['partidas']):
        gol = int(input(f'gol na partida {p + 1}º: '))
        gols.append(gol)

    for g in gols:
        gol_total += g

    jogador['gols_por_partida'] = gols
    jogador['gols_totais'] = gol_total
    time.append(jogador.copy())

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja cadastrar outro jogador? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('-' * 40)
print(f'{"ID":<4}{"NOME":<15}{"GOLS":<25}{"TOTAL":>5}')
print('-' * 40)
for i, jog in enumerate(time):
    print(f'{i:<4}{jog["nome"]:<15}{str(jog["gols_por_partida"]):<25}{jog["gols_totais"]:>5}')
print('-' * 40)

while True:
    busca = int(input("Mostrar dados de qual jogador? (Digite o ID ou 999 para sair): "))

    if busca == 999:
        break

    if 0 <= busca < len(time):
        jogador_selecionado = time[busca]
        print(f'-- LEVANTAMENTO DO JOGADOR {jogador_selecionado["nome"].upper()}:')

        # Exibe os gols de cada partida
        for i, g in enumerate(jogador_selecionado['gols_por_partida']):
            print(f'   => Na partida {i + 1}, fez {g} gol(s).')

        print(f"Total de Gols: {jogador_selecionado['gols_totais']}")
        print('-' * 40)
    else:
        print(f"ERRO! Não existe jogador com o ID {busca}. Tente novamente.")

