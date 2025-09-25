print('=== ex 086 ===')

matriz = [[], [], []]
for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha].append(valor)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[ {matriz[linha][coluna]:^5} ]', end='')
    print()