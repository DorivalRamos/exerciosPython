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


# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

from random import randint
from time import sleep


def func_1():
    n1 = n2 = n3 = randint(0, 10)
    soma = n1 + n2 + n3
    return soma


print(f'''
{'-='*26}
O valor Retornou {func_1()}
{sleep(1)}
{'-='*26}
''')
