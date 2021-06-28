# 3. Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

from random import randint, random


def somaImposto():
    taxaImposto = randint(1, 10) / 100 + 1
    item = randint(10, 100)
    return f''' 
     o item Custa {item} e com a taxa ele ficará por {item * taxaImposto:.2f} logo o a taxa foi de {taxaImposto - 1:.2f}%'''


print(somaImposto())
