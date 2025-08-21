print('=== ex 031 (Calculo Viagem) ===')

distancia = int(input('Qual a distancia da sua viagem? '))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print(f'O valor da Viagem é de R${valor}')

