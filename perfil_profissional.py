print('=== ex 092 ===')

dados = dict()

dados['nome'] = input("Nome: ")
ano_nasc = int(input("Ano de nascimento: "))
ano_atual = int(input("Ano atual: "))

dados['idade'] = ano_atual - ano_nasc
dados['ctps'] = int(input("Carteira de trabalho (0 se não tiver): "))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input("Ano de contratação: "))
    dados['salario'] = float(input("Salário: R$ "))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - ano_atual)

print(f"\nNome: {dados['nome']}")
print(f"Idade: {dados['idade']} anos")
print(f"CTPS: {dados['ctps']}")

if dados['ctps'] != 0:
    print(f"Ano de contratação: {dados['contratacao']}")
    print(f"Salário: R$ {dados['salario']:.2f}")
    print(f"Idade de aposentadoria: {dados['aposentadoria']} anos")

