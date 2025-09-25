print('=== 085 ===')

lista = [[],[]]
valor = 0
for c in range(7):
    valor = int(input(f'Digite o {c+1}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(lista)
print(f'Lista Pares: {lista[0]}')
print(f'Lista Impares: {lista[1]}')