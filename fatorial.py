print('=== ex 060 ===')

n = int(input("Digite um número: "))
fatorial = 1
contador = n

if n < 0:
    print("Fatorial não é definido para números negativos.")
elif n == 0:
    print("Fatorial de 0 é 1")
else:
    print("\nCalculando o fatorial de {}...".format(n))
    while contador > 1:
        fatorial *= contador
        print("\t{} x → acumulado = {}".format(contador, fatorial))
        contador -= 1
    print("\nFatorial de {} é {}".format(n, fatorial))
