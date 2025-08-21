from os.path import split

print('=== ex 022 ===')

frase = str(input('Digite um nome completo: '))

print(frase.upper())

print(frase.lower())

print(len(frase))

#qunats letras tem o primeiro nome?
primeiro_nome = frase.split()[0]
print('O primeiro nome tem {} letras'.format(len(primeiro_nome)))
print(primeiro_nome)