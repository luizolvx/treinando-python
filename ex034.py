print('=== ex 034 ===')

salario = float(input('DIGITE O VALOR DO SALÁRIO: '))

if salario > 1250.00:
    reajuste = salario * 0.10
else:
    reajuste = salario * 0.15

novo_salario = salario + reajuste

print(f'O reajuste salarial foi de R${reajuste:.2f}. Agora o seu SALÁRIO é de R${novo_salario:.2f}')
