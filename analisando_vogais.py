print('=== ex 078 ===')

lista = ('cachorro', 'peixe', 'gato', 'leao', 'girafa')

for palavra in lista:
    vogais = ''
    for letra in palavra:
        if letra.lower() in 'aeiou':
            vogais += letra
    print(f'{palavra.upper():<10} → Vogais: {", ".join(vogais)}')