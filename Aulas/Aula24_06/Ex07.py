# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois.
# Se eles forem iguais, imprima que eles são iguais.


from time import sleep


def min_func(n1, n2):
    if n1 == n2:
        return f'Eles são iguais'
    elif n1 < n2:
        return f'{n1} é menor '
    else:
        return f'{n2} é o menor'


n1 = int(input("Digite o 1° numero"))
sleep(1)
n2 = int(input("Digite o 2° numero"))
sleep(1)
print(f'''
O primeiro numero é {n1} {sleep(1)}
O segundo numero é {n2} {sleep(1)}
{min_func(n1 , n2)}
''')
