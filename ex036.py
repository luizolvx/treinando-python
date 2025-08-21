print('=== ex 036 Empréstimo Bancário ===')

valor = float(input('Digite o Preço da casa: '))
salario = float(input('Digite o Salário do Comprador: '))
prazo = float(input('Digite em Quantos Anos será pago: '))

prestacao_mensal = valor / (prazo * 12)

if prestacao_mensal > salario + salario * 0.3:
    print('O Seu Impréstimo foi NEGADO! A sua Prestação Mensal excede O Seu Salário em 30% ou mais')
else:
    print('O Seu Impréstimo foi Aprovado!!')

