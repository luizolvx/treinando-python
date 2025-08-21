print('=== ex 037 Base da Conversão ===')

numero = int(input('Digite um número inteiro: '))

print('Escolha a base de conversão:')
print('[1] Binário')
print('[2] Octal')
print('[3] Hexadecimal')

opcao = input('Sua opção: ')

# Realiza a conversão com base na escolha
if opcao == '1':
    print(f'{numero} convertido para BINÁRIO é {bin(numero)[2:]}')
elif opcao == '2':
    print(f'{numero} convertido para OCTAL é {oct(numero)[2:]}')
elif opcao == '3':
    print(f'{numero} convertido para HEXADECIMAL é {hex(numero)[2:].upper()}')
else:
    print('Opção inválida. Tente novamente.')

