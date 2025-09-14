print('ex 048')
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        print(c)
print('A soma de Todos dos Numeros Impares múltiplos de 3 no interavlo de 1 a 500 é: {}' .format(s))
print("FIM!!")