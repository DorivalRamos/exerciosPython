# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.

from random import randint


def func_1():
    n1 = randint(-10, 10)
    if n1 > 0:
        return f'{n1} é Positivo'
    elif n1 < 0:
        return f'{n1} é Negativo'

    if n1 == 0:
        return f'{n1} é Neutro'


print(func_1())
