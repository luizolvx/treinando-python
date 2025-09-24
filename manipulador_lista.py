from itertools import count

print('=== ex 081 ===')

lista = []
print('Digite 0 zero pra sair\n')
while True:
    numero = int(input('Digite um Número: '))
    lista.append(numero)

    if numero == 0:
        lista.remove(0)

        print('Encerrenado Programa...')

        contagem = 0
        for c in range(len(lista)):
            while contagem != len(lista):
                contagem += 1

        if 5 not in lista:
            print('O valor 5 não foi Digitado!')
        else:
            print('O valor 5 foi adicionado a Lista, pois não foi digitado!')


        lista.sort(reverse=True)
        print(f'Lista = {" " * 4}{lista}')
        print(f'tamanho:{contagem:>5}')
        break




