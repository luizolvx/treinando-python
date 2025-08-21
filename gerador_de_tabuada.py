print('=== ex 009 ===')

numero = int(input('Digite um Valor: '))

print('Tabuada do numero: {}'.format(numero))
for i in range(1, 11):
    resultado = numero * i
    print('{} x {} = {}'.format(numero, i, resultado))