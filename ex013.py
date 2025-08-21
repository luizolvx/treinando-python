print('=== ex 013 ===')
sal = int(input('Digite o valor do Salário: '))

aumento = sal * 5 / 100
sal = sal + aumento

print('Valor do Aumento: R$ {:.2f}'.format(aumento))
print('Salário depois do Aumento: R$ {:.2f}'.format(sal))
