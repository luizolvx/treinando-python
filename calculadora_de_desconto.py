print('=== ex 012 ===')
num = int(input('Digite o valor do produto: '))

desconto = num * 5 / 100
num = num - desconto

print('Valor do Desconto: R$ {:.2f}'.format(desconto))
print('Produto com desconto: R$ {:.2f}'.format(num))
