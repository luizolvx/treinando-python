from random import randint
print('=== ex 074 ===')

tupla_numeros = tuple(randint(1, 100) for i in range(5))
print(tupla_numeros)