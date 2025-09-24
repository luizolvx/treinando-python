print('=== ex 79 ===')

lista = []

for i in range(5):
    numero = int(input('Digite um Número: '))
    if numero not in lista:
        lista.append(numero)
        print('Valor adicionado com sucesso...')
        opcao = input('Deseja continuar? [S/N] ').upper()
    elif opcao == 'N':
        break
    else:
        print('Valor Duplicado! Não vou adcionar')

print('\nLista em Ordem Crescente:', sorted(lista))
print('Lista em Ordem Decrescente:',sorted(lista, reverse=True))
