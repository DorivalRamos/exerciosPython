# Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if, verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade' e  também quantos são maiores e quantos são menores de idade.

# from time import sleep
# galera = list()
# tmaior = tmenor = 0

# for c in range(3):
#     nome = str(input("Digite o nome: "))
#     idade =int(input("Digite a idade: "))
#     galera.append([nome , idade])

# for p in galera:
#     sleep(1)
#     if p[1] >= 18:
#         print(f"{p[0]} é maior de idade")
#         tmaior = tmaior + 1
#     else:
#         print(f"{p[0]} é menor de idade")
#         tmenor = tmenor + 1

# print(f" Temos {tmaior} maiores e {tmenor} menores de idade")


# Exercicios:

# #01 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com essa formatação:

# [  1  ][  2  ][  3  ]
# [  4  ][  5  ][  6  ]
# [  7  ][  8  ][  9  ]
# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(f" {matriz[0]}\n {matriz[1]}\n {matriz[2]}\n")

# 02 - Aprimore o desafio anterior, mostrando no final:
#  A) A soma de todos os valores pares digitados.
#  B) A soma dos valores da terceira coluna.
#  C) O maior valor da segunda linha.

# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(f" {matriz[0]}\n {matriz[1]}\n {matriz[2]}\n")

# print(
#     f"A soma de todos os valores pares digitados. {matriz[0][1] + matriz[1][0]  + matriz[1][2] + matriz[2][1]}")
# print(
#     f"A soma dos valores da terceira coluna. {matriz[0][2] + matriz[1][2] + matriz[2][2]}")
# print(f"O maior valor da segunda linha.{matriz[1][2]}")


# 03 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista, depois do dado inserido, pergunte ao usuário se ele quer continuar, se ele não quiser pare o programa. No final mostre:
# Quantas pessoas foram cadastradas
# Mostre o maior peso
# Mostre o menor peso


galera = list()
minPeso = maxPeso = 0
while True:
    nome = str(input("Digite o nome da pessoa: "))
    peso = int(input("Digite o peso: "))
    galera.append([nome, peso])
    parar = str(input("Deseja parar ?[S/N}").upper())
    if parar.startswith('S'):
        break

for c in enumerate(galera):
    print(f"Quantas pessoas foram cadastradas? {len(galera)}")
    print(f"{min(galera[1])}")
