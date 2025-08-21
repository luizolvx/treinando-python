print('=== ex042 Tipo do Triângulo ===')

lado1 = float(input('Digite o Lado do Triangulo: '))
lado2 = float(input('Digite o Lado do Triangulo: '))
lado3 = float(input('Digite o Lado do Triangulo: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('A retas PODEM Formar um triangulo')
    if lado1 == lado2 and lado1 == lado3:
        print('O Triângulo é EQUILÁTERO')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('O Triângulo é ISÓCELES')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('O Triângulo é ESCALENO')
else:
    print('A retas NÃO podem Formar um triangulo')