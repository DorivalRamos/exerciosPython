# 1. Exercício Treino - Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes aos quadrados desses números.
# {1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81}

# dicionario = dict({
#     1: 1,
#     4: 16,
#     5: 25,
#     6: 36,
#     7: 49,
#     9: 81
# })

# print(dicionario)


# 2. Exercício Treino - Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10] e cada valor associado é o número ao quadrado.
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# dicionario = dict({
#     1: 1,
#     2: 4,
#     3: 9,
#     4: 16,
#     5: 25,
#     6: 36,
#     7: 49,
#     8: 64,
#     9: 81,
#     10: 100
# })

# print(dicionario)

# 3. Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado.

# aluno = dict()
# aluno['nome'] = str(input("Digite o Nome do aluno: "))
# aluno['media'] = float(input(f"Digite a média do {aluno['nome']}: "))

# if aluno['media'] < 5:
#     aluno['nota'] = "Reprovado"
# elif aluno['media'] >= 7:
#     aluno['nota'] = "Aprovado"
# else:
#     aluno['nota'] = "Recuperação"

# print(
#     f"O aluno {aluno['nome']} esta com a nota {aluno['media']} e esta {aluno['nota']}!!!!!")


# 4. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.


# from datetime import date
# anoAtual = date.today().year
# aposentadoria = int(0)

# trabalhador = dict()
# trabalhador['nome'] = str(input("Digite seu nome: "))
# trabalhador['idade'] = int(
#     input(f"{trabalhador['nome']} digite o seu ano de nascimento: "))
# trabalhador['ctps'] = int(
#     input(f"{trabalhador['nome']} digite o seu ctps, caso não tenha digite 0 : "))
# trabalhador.setdefault('contratação', 35)


# if trabalhador['ctps'] != 0 or None:
#     trabalhador['contratação'] = int(
#         input(f"{trabalhador['nome']} digite o ano de contratação: "))
#     salario = int(input(f"{trabalhador['nome']} digite seu salario: R$"))
#     aposentadoria = anoAtual - trabalhador['contratação']
# print(f'''
# Você {trabalhador['nome']},
# Possue {anoAtual - trabalhador['idade'] } anos,
# você vai se aposentar com {(anoAtual - trabalhador['idade']) - aposentadoria  +35 }  anos
# ''')


# 5. DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.

from time import sleep

dictPessoa = dict()
listPessoa = list()

while True:
    dictPessoa['nome'] = str(input("Digite seu nome: "))
    dictPessoa['sexo'] = str(
        input(f"{dictPessoa['nome']} digite o seu sexo [M/F]: ")).upper().split()[0]
    dictPessoa['idade'] = int(
        input(f"{dictPessoa['nome']} digite sua idade: "))
    parar = str(input("Você deseja para ?[S/N]: ")).upper()

    print(dictPessoa['sexo'])

    while (dictPessoa['sexo'] != 'M') and (dictPessoa['sexo'] != 'F'):
        dictPessoa['sexo'] = str(input("Por favor Digite o sexo certo [M/F]"))
        print(dictPessoa['sexo'])

    listPessoa.append(dictPessoa.copy())
    if parar.startswith('S'):
        break
print(f'''
Quantas pessoas estão cadastradas {len(listPessoa)}
A média da idade. {sum(listPessoa['idade']) / len(listPessoa['idade'])}


''')
