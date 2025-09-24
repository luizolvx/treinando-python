print('=== ex 083 ===')
caracteres = []

frase = str(input('Digite uma frase dentro de parênteses: '))

caracteres = list(frase)
print(caracteres)

if caracteres[0] == '(' and caracteres[-1] == ')':
    print('A ordem dos Parênteses está CERTA!')
elif caracteres[0] == ')' and caracteres[-1] == '(':
    print('A ordem dos Parênteses está ERRADA!!')
else:
    print('A ordem dos Parênteses está ERRADA!')
