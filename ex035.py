print('=== ex 035 ===')

lado1 = int(input('Digite o Lado do Triangulo: '))
lado2 = int(input('Digite o Lado do Triangulo: '))
lado3 = int(input('Digite o Lado do Triangulo: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('A retas PODEM Formar um triangulo')
else:
    print('A retas NÃO podem Formar um triangulo')