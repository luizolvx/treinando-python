print('=== ex 076 ===')

feira = (('Banana', 8.5), ('Maça', 5.8), ('Pera', 12.5), ('Suco', 9.8))

print('-'*30)
for item , preco in feira:
    print(f'{item:<10} | R$ {preco:>5.2f}')
print('-'*30)

listagem = ('Banana', 8.5, 'Leite', 3.50, 'Frango', 10.90)
print('\n\n')
print('ITEM      | PREÇO')
print('-' * 22)

for i in range(0, len(listagem), 2):
    produto = listagem[i]
    preco = listagem[i + 1]
    print(f'{produto:<10} | R$ {preco:>5.2f}')
