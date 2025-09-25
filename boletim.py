boletim = []

while True:
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2

    boletim.append([nome, [nota1, nota2], media])

    opc = input("Quer continuar? [S/N] ").strip().upper()
    if opc == "N":
        break

print("\n--- BOLETIM ---")
print(f"{'Nº':<4}{'Nome':<15}{'Média':>8}")
print("-" * 30)
for i, aluno in enumerate(boletim):
    print(f"{i:<4}{aluno[0]:<15}{aluno[2]:>8.1f}")

while True:
    opc = int(input("\nMostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        print("Finalizando...")
        break
    if opc < len(boletim):
        print(f"Notas de {boletim[opc][0]} são {boletim[opc][1]}")
