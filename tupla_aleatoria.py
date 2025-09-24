from random import randint
print('=== ex 074 ===')

tupla_numeros = tuple(randint(1, 100) for i in range(5))
print(tupla_numeros)

ordem = sorted(tupla_numeros)
print('Tupla organizada em ordem Crescente:', ordem)
print('Esse é o Maior Número da Tupla',ordem[-1])
print('Esse é o Menor Número da Tupla',ordem[0])