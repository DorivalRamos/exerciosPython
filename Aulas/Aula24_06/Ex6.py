# Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).

from random import randint


def nota_func():
    nota = randint(0, 10)
    if nota >= 9:
        return f'Sua nota foi {nota} =A'
    elif nota >= 8:
        return f'Sua nota foi {nota} =B'
    elif nota >= 7:
        return f'Sua nota foi {nota} =C'
    elif nota >= 6:
        return f'Sua nota foi {nota} = D'
    elif nota >= 5:
        return f'Sua nota foi {nota} = E'
    else:
        return f'Sua nota foi {nota} = F'


print(nota_func())
