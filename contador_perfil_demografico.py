print('=== ex 069 ===')
maioridade = 0
homens = 0
mulheres_subvinte = 0
while True:
    print('-' * 23)
    print('CADASTRE UMA PESSOA')
    print('-' * 23)
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo (M/F): ')).upper()


    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_subvinte += 1

    opcao = str(input('Você quer Continuar? [S/N]')).upper()

    if opcao == 'N':
        print('\n\t --- Resultado do Perfil Demográfico ---')
        print('Pessoas acima dos 18: {}'.format(maioridade))
        print('Homens: {}'.format(homens))
        print('Mulheres com menos de 20 anos de idade: {}'.format(mulheres_subvinte))
        break

