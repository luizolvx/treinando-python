print('=== ex 075 ===')

tupla = ()
for i in range (4):
    numero = int(input('Digite um número: '))
    tupla += (numero,) # a ',' Adiciona o número à tupla

print('O número 9 aparece:', tupla.count(9), 'vezes')

if 3 in tupla:
    print('O número 3 aparece na posição:', tupla.index(3))
else:
    print('O número 3 não foi digitado.')

print('Tupla =',tupla)

print('Números pares e seus índices:')
for indice, valor in enumerate(tupla):
    if valor % 2 == 0:
        print(f'Número par {valor} na posição {indice}')