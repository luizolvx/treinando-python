print('=== ex 093 ===')
gol_total = 0
jogador = dict()
gols = list()

jogador['nome'] = str(input('Nome: '))
jogador['partidas'] = int(input('partidas: '))

for p in range(jogador['partidas']):
    gol = int(input(f'gol na partida {p+1}º: '))
    gols.append(gol)


for g in gols:
    gol_total += g

jogador['gols_por_partida'] = gols
jogador['gols_totais'] = gol_total


print('\n Dados do jogador:')
print(f"Nome: {jogador['nome']}")
print(f"Partidas jogadas: {jogador['partidas']}")
print(f"Gols por partida: {jogador['gols_por_partida']}")
print(f"Gols no Campeonato: {jogador['gols_totais']}")