# Exercicio 1

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

# from random import sample
# perguta = int(input("Quantos jogos você quer que crie ?"))
# for c in range(perguta):
#     print(sorted(sample(range(1, 60), 6)))
