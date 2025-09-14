print('=== 067 ===')
numero = 0
print(f'\t Tabuada do {numero}')

while True:
    numero = int(input('Digit o numero base da tabuada: '))
    if numero < 0:
        print('Encerrando...')
        break
    print(f'\t Tabuada do {numero}')
    numero_tabuada = 1
    while numero_tabuada <= 10:
        resultado  = numero * numero_tabuada
        print(f"{numero} x {numero_tabuada} = {resultado}")
        numero_tabuada += 1

