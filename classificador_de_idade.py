import datetime
print('=== ex041 Categoria Idade')
ano_nascimento = int(input('Digite o Ano em que Você Nasceu:  '))
ano_atual = datetime.date.today().year

idade = ano_atual - ano_nascimento

if idade <= 9:
    print('Categoria Mirim')
elif idade <= 14:
    print('Categoria Infantil')
elif idade <= 19:
    print('Categoria Junior')
elif idade == 20:
    print('Categoria Senior')
else:
    print('Categoria Master')

