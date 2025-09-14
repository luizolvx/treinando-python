print("ex 052")
n = int(input("Digite um número: "))

total_divisores = 0

for c in range(1, n + 1):
    if n % c == 0:
        total_divisores += 1

if total_divisores == 2:
    print(f"O número {n} é primo.")
else:
    print(f"O número {n} não é primo.")