from turtledemo.penrose import start

print('=== ex 073 ===')
brasileirao = ('corinthians', 'flamengo', 'inter', 'cruzeiro', 'gois', 'atl.mineiro', 'atl.paranaense', 'vasco', 'santos', 'são paulo', 'criciuma', 'portuguesa', 'ferroviaria', 'madureira', 'figueirense','criciuma','nautico', 'bahia', 'fortaleza', 'vitoria', 'palmeiras')
for posicao, times in enumerate(brasileirao[:5]):
    print(f'{posicao + 1}° colocado -',times)

print('\n')
for posicao, times in enumerate(brasileirao[16:], start=15):
    print(f'{posicao + 1}° colocado -',times)

print('\n')
alfabetica = sorted(brasileirao)
print('Times em ordem alfabética:')
for time in alfabetica:
    print(time)

print('\n')
print(alfabetica)
