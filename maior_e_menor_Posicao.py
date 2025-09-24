print('=== ex 078 ===')
lista = []

for c in range(5):
    numero = int(input('Digite um numero: '))
    lista.append(numero)

maior = lista[0]
menor = lista[0]
pos_maior = 0
pos_menor = 0
for x, n in enumerate(lista):
    if n > maior:
        maior = n
        pos_maior = x
    elif n < menor:
        menor = n
        pos_menor = x
print(lista)

print(f'Maior: {maior} na Posição {pos_maior}')
print(f'Menor: {menor} na Posição {pos_menor}')

