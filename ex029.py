from random import randint

print('=== 029 ===')

velocidade = randint(0, 200)
if velocidade > 80:

    print('MULTADO!! Você EXCEDEU o limite de velocidade do Radar!')
    print('A multa vai custar 7 reais')
else:
    print('Você está DENTRO dos limites de velocidade do Radar!')
print('A Sua Velocidade é de {}Km/h' .format(velocidade))