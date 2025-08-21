print('=== ex 043 Cáçculo do IMC ===')

peso = float(input('Digite o Peso em Kg: '))
altura = float(input('Digite a Altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('ABAIXO do Peso')
elif imc >= 18.5 and imc < 24.9:
    print('Peso NORMAL')
elif imc >= 25 and imc < 29.9:
    print('SOBREPESO')
elif imc >= 30 and imc < 34.9:
    print('OBESIDADE grau I')
elif imc >= 35 and imc < 39.9:
    print('OBESIDADE grau II')
else:
    print('OBESIDADE grau III')