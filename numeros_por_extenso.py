print('=== 072 ===')
valores = 0
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'novem', 'dez', 'onze', 'doze', 'treze', 'catorze','quinze','dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    numero = int(input('Digite um Número de 0 a 20: '))
    if numero < 0 or numero > 20:
        print('\nNecessário Digitar um valor entre 0 e 20')
        print('Encerrando o Programa...')
        break
    valores = tupla[numero]
    print(tupla[numero])