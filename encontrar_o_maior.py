print('=== ex 033 ===')
num1 = int(input('Digite o Primeiro Número: '))
num2 = int(input('Digite o Segundo Número: '))
num3 = int(input('Digite o Terceiro Número: '))

if num1 > num2 and num1 > num3:
    print('O primeiro Número é o maior')
elif num2 > num1 and num2 > num3:
    print('O Segundo Número é o maior')
else:
    print('O Terceiro Número é o maior')