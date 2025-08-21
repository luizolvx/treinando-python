print('=== ex 015 ===')

dias = float(input('Digite a quantidade de dias Alugados: '))
km = float(input('Digite o valor dos Km percorridos: '))

valor = (km * 0.15) + (dias * 60)
print('Valor do Produto: R$ {:.2f}'.format(valor))