print('=== ex 023 ===')
numero = input('Digite um numero de 0 a 9999: ')

# Pad the number with leading zeros to ensure it always has 4 digits
numero_formatado = numero.zfill(4)

print(f'Unidade: {numero_formatado[3]}')
print(f'Dezena: {numero_formatado[2]}')
print(f'Centena: {numero_formatado[1]}')
print(f'Milhar: {numero_formatado[0]}')