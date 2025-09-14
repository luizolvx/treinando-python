print('=== ex 063 ===')

primeiro = int(input("Digite o primeiro número da sequência: "))
segundo = int(input("Digite o segundo número da sequência: "))
quantidade = int(input("Quantos termos você quer mostrar? "))

contador = 0

print("\nSequência de Fibonacci personalizada:")
while contador < quantidade:
    print("Termo {}: {}".format(contador + 1, primeiro))
    proximo = primeiro + segundo
    primeiro = segundo
    segundo = proximo
    contador += 1
