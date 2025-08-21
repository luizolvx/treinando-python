import random

alunos = ["matheus", "igor", "felipe", "ryan"]  # agora é uma lista
random.shuffle(alunos)

print('O primeiro a ser sorteado foi o {}'.format(alunos[0]))
print('O segundo a ser sorteado foi o {}'.format(alunos[1]))
print('O terceiro a ser sorteado foi o {}'.format(alunos[2]))
print('O quarto a ser sorteado foi o {}'.format(alunos[3]))
