# lista = list()
# lista.append(4)  # Adiciona um valor no fim da lista
# lista.insert(1,23) # Adiciona na posição que você quise,sem substituir o valor dentro da lista
# del lista[3] #Deleta o item da posição selecionada!
# lista.pop() #apaga o ultimo valor ou uma posição especifica!!
# lista.remove() #remove pelo primeiro valor encontrado

# print(lista)
# print(sorted(lista)) # cria uma lista em ordem crescente
# print(sorted(lista), reversed=True) #cria uma lista em ordem descrecente

# a = [1,2,3]
# b = a
# b = a #espelhas as duas listas
# b = a[:] #cria uma copia

# lista[2] = str('dorival')
# print(lista)

# lista.append(int(input("Digite o numero")))

# for posição, valor in enumerate(a):
#   print(f"A posição de {valor} é a {posição}")


# lista = [5, 7, 2, 9, 4, 1, 3]
# print(f'''
#   a) tamanho da lista {len(lista)}\n
#   b) maior valor da lista {sorted(lista)[-1]}\n
#   c) menor valor da lista {sorted(lista)[0]}\n
#   d) soma de todos os elementos da lista
#   \n
#   e) lista em ordem crescente {sorted(lista)}\n
#   f) lista em ordem decrescente {sorted(lista)[::-1]}

#   ''')

# lista = ("Telefonou para a vítima?", "Esteve no local do crime?",
#          "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?")
# n2 = int()
# for posição, valor in enumerate(lista):
#     n1 = input(f"{valor} [S/N]: ").lower().split()[0]

#     if n1 == 's':
#         n2 = n2 + 1

# if n2 <= 1:
#     print("Inocente")
# elif n2 == 2:
#     print("Suspeita")
# elif n2 == 5:
#     print("Assassino")
# else:
#     print(
#         "Cúmplice"
#     )
