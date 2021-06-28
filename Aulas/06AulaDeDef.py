# Funções!

# Gerador de nomes aleatorios
# pip install names
# from names import get_first_name

# nome = get_first_name()
# print(nome)


# Faça um programa, com uma função que necessite de um parametro. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.


# def positivo(n1)

#     if n1 % 2 == 0:
#         return f'Positivo'
#     else:
#         return f'Negativo'

#n1 = int(input("Digite um numero para saber se ele é numero é par: "))
# print(positivo())


# Faça um programa em Python com uma função que necessite de três parametros, e que forneça:
# A soma desses três parametros através de uma função.
# Seu script também deve fornecer a média dos três números,  através de uma segunda função que chama a primeira.

# from random import randint


# def fun1(n1, n2, n3):
#     res = n1 + n2 + n3
#     return res


# def fun2(somas):
#     med = somas / 3
#     return f'A média é {med:.2f}'


# def menu():
#     n1 = randint(9, 10)
#     n2 = randint(1, 10)
#     n3 = randint(1, 10)
#     somar = fun1(n1, n2, n3)
#     print(fun2(somar))


# menu()
