print("=== ex 070 ===")
print('=== Caixa Eletrônico ===')

while True:
    valor = int(input('Digite o valor que deseja sacar (ou 0 para sair): R$'))
    if valor == 0:
        print('Encerrando o caixa. Volte sempre!')
        break

    total = valor
    cedula = 50

    while True:
        quantidade = total // cedula
        total %= cedula

        if quantidade > 0:
            print(f'{quantidade} cédula(s) de R${cedula}')

        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        else:
            break

    print('-' * 30)
