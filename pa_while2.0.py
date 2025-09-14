print('=== ex 062 ===')


primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiro
total_termos = 0
mais_termos = 10  # Começa mostrando os 10 primeiros termos

while mais_termos != 0:
    total_termos += mais_termos
    contador = 1
    while contador <= mais_termos:
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1

    print('PAUSA')
    mais_termos = int(input('Quantos termos você quer mostrar a mais? '))

print('Progressão finalizada com {} termos mostrados.'.format(total_termos))