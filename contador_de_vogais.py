print('=== 077 ===')

palavras = ()
vogais = ()
vogais_total = 0

for x in range(5):
    palavra = str(input('Digite uma palavra: ')).lower()
    palavras += (palavra,)

    contador_vogais = 0
    for letra in palavra:
        if letra in 'aeiou':
            contador_vogais += 1

    vogais += (contador_vogais,)
    vogais_total += contador_vogais

print('\n\tVogais por Palavra')
for x in range(len(palavras)):
    print(f'{palavras[x]:<7}-> {vogais[x]}')

print(f'\nVogais totais: {vogais_total}')
