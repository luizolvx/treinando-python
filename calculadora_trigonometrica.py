import math

print('=== Cálculo de Seno, Cosseno e Tangente ===')

angulo = float(input('Digite um ângulo em graus: '))

# Converter para radianos
rad = math.radians(angulo)

# Calcular seno, cosseno e tangente
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

# Exibir os resultados com duas casas decimais
print('Para o ângulo de {:.2f}°:'.format(angulo))
print('Seno = {:.2f}'.format(seno))
print('Cosseno = {:.2f}'.format(cosseno))
print('Tangente = {:.2f}'.format(tangente))