import datetime
print('=== ex 039 Ano de Nascimento ===')

ano = int(input('Digite o Ano em que Nasceu: '))

ano_atual = datetime.date.today().year

idade = ano_atual - ano

if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para você se alistar!')
elif idade == 18:
    print('Você deve se alistar este ano!')
else:
    print(f'Já se passaram {idade - 18} anos do seu alistamento!')