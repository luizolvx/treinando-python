from random import randint

print('=== Radar de Velocidade ===')

velocidade = randint(0, 200)
limite = 80

if velocidade > limite:
    excedido = (velocidade - limite) * 100 / limite

    if excedido <= 20:
        multa = 130.16
        tipo = 'Média'
        pontos = 4
    elif excedido <= 50:
        multa = 195.23
        tipo = 'Grave'
        pontos = 5
    else:
        multa = 880.41
        tipo = 'Gravíssima'
        pontos = 7

    print(f'MULTADO! Você excedeu o limite de {limite}Km/h em {excedido:.2f}%.')
    print(f'Infração {tipo}: R$ {multa:.2f} e {pontos} pontos na CNH.')
else:
    print('Você está dentro do limite de velocidade.')

print(f'Sua velocidade: {velocidade}Km/h')
