print('=== 026 ===')

frase = input('Digite uma frase: ')

frase = frase.upper()

quantidade = frase.count('A')
print('A letra "A" aparece {} vezes'.format(quantidade))

primeira_posicao = frase.find('A')
print('A letra "A" aparece pela primeira vez na posição {}'.format(primeira_posicao))

ult_ocorre = frase.rfind('A')
print('A última ocorrencia de "a" foi na posição {}'.format(ult_ocorre))