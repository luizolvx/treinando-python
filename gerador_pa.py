print('Gerador de PA')

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

pa_string = ''

for i in range(10):
    termo = primeiro_termo + i * razao
    pa_string += str(termo)
    if i < 9:
        pa_string += ' -> '

print(pa_string)
print('FIM')