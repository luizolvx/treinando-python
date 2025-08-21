print('=== ex024 ===')

frase = input('Digite o Nome de uma Cidade: ')
frase_div = frase.split()[0]
frase_div = 'santo' in frase
print("TRUE = comça com 'Santo'/FALSE não começa com 'Santo'. resultado ->{}<-".format(frase_div))
