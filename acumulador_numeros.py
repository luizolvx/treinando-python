print('=== 066 ===')
numero = 0
soma = 0
print('Se quiser Parar Digite 999')
while True:
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    soma += numero
print('A soma dos numeros foi {}'.format(soma))
