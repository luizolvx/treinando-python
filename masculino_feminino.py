print('ex 057')

letra = str(input('Digite o seu sexo(M/F): ')).upper()

while letra != 'M' and letra != 'F':
    print('Digite "M" OU "F" pra indicar o seu sexo.')
    letra = str(input('Digite o seu sexo (M/F): ')).upper()

if letra == 'M':
    print('Masculino')
elif letra == 'F':
    print('Feminino')


