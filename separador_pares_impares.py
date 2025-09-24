print('=== ex 082 ===')
lista = []
for c in range(7):
    numero = int(input('digite um numero: '))
    lista.append(numero)

print(lista)
lista_pares = []
lista_impares = []

for i, c in enumerate(lista):
    if lista[i] % 2 == 0:
        lista_pares.append(c)
    if lista[i] % 2 != 0:
        lista_impares.append(c)
print('numero pares: {}'.format(lista_pares))
print('numero impares: {}'.format(lista_impares))

