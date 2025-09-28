print('=== ex 094 ===')
dados = list()
pessoa = dict()
cadastros = 0
for p in range (5):
    pessoa['nome'] = str(input('nome: '))
    pessoa['idade'] = int(input('idade: '))
    pessoa['sexo'] = str(input('sexo: [F/M]: ')).upper()
    dados.append(pessoa.copy())
    pessoa.clear()
    cadastros += 1
print('\n', '-='*7, 'DADOS DOS CADASTRADOS', '-='*7)
for p in dados:
    print('Cadastrado ->', p)
print('Total de cadastrados: {}'.format(cadastros))

soma_idade = 0
for p in dados:
    soma_idade += p['idade']
media = soma_idade / cadastros
print('media das idades: {}'.format(media))

acima_media = list()
for p in dados:
    if p['idade'] > media:
        acima_media.append(p['nome'])
print('Lista pessoas com idade acima da média: {}'.format(acima_media))
