print('=== ex 010 ===')

alt = int(input('Digite a Altura da Parede: '))
lar = int(input('Digite a Largura da Parede: '))

area = alt * lar
print('A Área da Parede em Metros é {}' .format(area))

tinta = area / 2
print('A Quantidade de tinta pra pintar a parede de {}m é igual a {}L' .format(area, tinta))