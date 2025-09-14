print('ex 050')
s = 0
for c in range(0, 6):
    n = int(input("Digite um Número: "))
    if n % 2 == 0:
        s += n
print("O valor da soma é: {}".format(s))
