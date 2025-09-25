print('=== ex 084 ===')

galera = list()
pessoa = list()

for c in range(0, 5):
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    galera.append(pessoa[:])
    pessoa.clear()

galera.sort(key=lambda p: p[1], reverse=True)

maior_peso = galera[0][1]
menor_peso = galera[-1][1]

mais_pesadas = []
mais_leves = []

for p in galera:
    if p[1] == maior_peso:
        mais_pesadas.append(p)
    elif p[1] == menor_peso:
        mais_leves.append(p)

print(f'\nTotal de pessoas cadastradas: {len(galera)}')
print(f'Maior peso: {maior_peso:.1f}Kg. Pessoas mais pesadas:')
for p in mais_pesadas:
    print(f' - {p[0]} com {p[1]:.1f}Kg')

print(f'\nMenor peso: {menor_peso:.1f}Kg. Pessoas mais leves:')
for p in mais_leves:
    print(f' - {p[0]} com {p[1]:.1f}Kg')
