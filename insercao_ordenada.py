print('=== ex 080 ===')

lista = []
menor_numero = 0
for c in range(5):
    numero = int(input('digite um numero: '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                break
            posicao += 1
print('Lista ordenada:', lista)







