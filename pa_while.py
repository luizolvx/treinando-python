print('=== ex 061 ===')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiro
contador = 1

print('Os 10 primeiros termos da PA são:')
while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    contador += 1
print('FIM')