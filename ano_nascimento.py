print("ex 054")
for c in range(7):
    print('{}ª pessoa'.format(c+1))
    ano = int(input("Digite o ano de nascimento: "))
    if 2025 - ano  < 18:
        print('Menor de idade')
    else:
        print('Maior de idade')