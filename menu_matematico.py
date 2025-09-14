print('===ex 059 ===')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opcao = ''

while opcao != '5':
    print("\tMenu")
    print("[1]Somar")
    print("[2]Multiplicar")
    print("[3]Maior")
    print("[4]Novos Números")
    print("[5]Sair do programa")
    opcao = str(input('Digite um valor: '))

    if opcao == '1':
        soma = n1 + n2
        print("Soma: {}".format(soma))
    elif opcao == '2':
        multiplicacao = n1 * n2
        print("Multiplicacao: {}".format(multiplicacao))
    elif opcao == '3':
        maior = n1 if n1 > n2 else n2
        print("Maior: {}".format(maior))
    elif opcao == '4':
        n1 = int(input('Digite um NOVO valor: '))
        n2 = int(input('Digite um NOVO outro valor: '))
    elif opcao == '5':
        print('Obrigado por usar o programa!')




