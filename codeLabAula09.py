# Exercicio 1
# 01 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# lista = list()
# while True:
#     per = input(
#         "Digite um número por vez quando desejar parar eu vou mostrar elas em ordem crescente: ")
#     if per not in lista:
#         lista.append(per)
#     per2 = input("Deseja continuar ?[S/N]").lower()
#     if per2.startswith('n'):
#         break

# print(sorted(lista))


# Excercicio 2
# Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.

# lista = list()
# listaPar = list()
# listaImp = list()
# while True:
#     pergunta = int(input(
#         "Digite um número por vez quando desejar parar eu vou mostrar elas em Três listas: uma inteira e duas separadas em pares e impares: "))
#     lista.append(pergunta)

#     if pergunta % 2 == 0:
#         listaPar.append(pergunta)
#     else:
#         listaImp.append(pergunta)
#     pergunta2 = input("Deseja parar?[S/N]: ").lower()
#     if pergunta2.startswith('s'):
#         break

# print(f'''
#     A lista completa{sorted(lista)},\n
#     A lista do Par{sorted(listaPar)},\n
#     A lista do Impar{sorted(listaImp)}
# ''')


# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# from random import sample
# lista = list()
# perguta = int(input("Quantos jogos você quer que crie ?"))
# for c in range(perguta):
#     lista2 = (sorted(sample(range(1, 61), 6)))
#     lista.append(lista2)

# print(lista)

# from random import sample
# perguta = int(input("Quantos jogos você quer que crie ?"))
# for c in range(perguta):
#     print(sorted(sample(range(1, 60), 6)))
