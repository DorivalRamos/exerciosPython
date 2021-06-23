# () Tuplas, [] lista, {} dicionario


# dados = dict(
#   {
#     "nome" : " ",
#     "idade" : " ",
#     "peso" : " ",
#   }
# )

# if dados.get("nome") == None:# para pegar o dado dentro do disc e não crachar
#   print('não existe')
#   dados.setdefault("altura", 1.70)
# else:
#   print(f"{dados.get('nome')}")

# value()= Valores do dicionario em formato de lista
# keys()= As chavez em formato de lista
# itens()= retorna uma tupla dentro de lista contendo as keys com os values


# aluno = dict()
# aluno['nome'] = str(input("Digite o nome do aluno: "))
# aluno['media'] = float(input(f"Media do {aluno['nome']}: "))

# if aluno['media'] >= 7:
#     aluno['situação'] = "Aprovado"
# elif 5 <= aluno['media'] < 7:
#     aluno['situação'] = "Recuperação"
# else:
#     aluno['situação'] = "Reprovado"


# for k, v in aluno.itens():
#     print(f"{k} é igual a {v}")

import datetime

trabalhador = dict()
trabalhador['nome'] = str(input("Digite seu nome: "))
trabalhador['idade'] = int(
    input(f"{trabalhador['nome']} digite o seu ano de nascimento: "))
trabalhador['ctps'] = int(
    input(f"{trabalhador['nome']} digite o seu ctps, caso não tenha digite 0 : "))
trabalhador.setdefault('contratação', 35)


if trabalhador['ctps'] != 0 or None:
    trabalhador['contratação'] = int(
        input(f"{trabalhador['nome']} digite o ano de contratação: "))
    salario = int(input(f"{trabalhador['nome']} digite seu salario: R$"))

print(f''' 
Você {trabalhador['nome']},
Possue {trabalhador['idade'] - datetime.y} anos,
você vai se aposentar com {trabalhador['idade'] - datetime.year} + {trabalhador['contratação'] - datetime.year} + 35 anos 
''')
