print('=== ex 044 Valor á ser pago (À vista, Cartão, Parcelado)===')

preco_produto = float(input('Preço do Produto: '))

print('\tFormas de Pagamento: ')
print('[1] Dinheiro À Vista')
print('[2] Cartão À vista')
print('[3] Parcelar Duas Vezes')
print('[4] Parcelar Três Vezes')

opcao = input('Digite o Número da Opção Escolhida!')

if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4':
    print('\tOpção INVÁLIDA!!')
else:
    if opcao == '1':
        avista_dinheiro = preco_produto - (preco_produto * 0.10)
        print('O Valor Ficou em R$ {:.2f}'.format(avista_dinheiro))
    elif opcao == '2':
        avista_cartao = preco_produto - (preco_produto * 0.05)
        print('O valor Ficou em R$ {:.2f}'.format(avista_cartao))
    elif opcao == '3':
        parcelado_duas = preco_produto / 2
        print('O valor Ficou em R$ {:.2f}' .format(parcelado_duas))
    elif opcao == '4':
        parcelado_tres = preco_produto + (preco_produto * 0.20)
        print('O Valor Ficou em R$ {:.2f}'.format(parcelado_tres))