print('=== ex 087 ===')

matriz = [[], [], []]
soma_pares = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha].append(valor)
        if valor % 2 == 0:
            soma_pares += valor

print('\nMatriz digitada:')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[ {matriz[linha][coluna]:^5} ]', end='')
    print()

soma_terceira_coluna = 0
for linha in range(0, 3):
    soma_terceira_coluna += matriz[linha][2]

maior_valor_segunda_linha = max(matriz[1])

print(f'\nSoma dos valores pares: {soma_pares}')
print(f'Soma dos valores da terceira coluna: {soma_terceira_coluna}')
print(f'Maior valor da segunda linha: {maior_valor_segunda_linha}')
