print("ex 054")
frase = str(input("Digite uma frase: ")).strip().upper()

frase_sem_espacos = frase.replace(" ", "")

frase_invertida = frase_sem_espacos[::-1]

if frase_sem_espacos == frase_invertida:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")