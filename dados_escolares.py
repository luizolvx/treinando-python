print('=== ex 090 ===')

turma = list()
aluno = dict()

for a in range(3):
    aluno['nome'] = str(input('Nome: '))
    aluno['nota'] = float(input('Nota: '))
    aluno['situacao'] = str(input('Situação(Aprov/Reprov/Recup): '))
    turma.append(aluno.copy())
for aluno in turma:
    print(aluno)