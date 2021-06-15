# 01 - Faça um programa que leia o sexo biológico de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto

# sexo = input("Qual o seu sexo Biológico?[M/F]: ").upper().strip()[0]

# while sexo not in "MF":
#     print("Digite o Sexo Biológico Valido!!")
#     sexo = input("Qual o seu sexo Biológico?[M/F]: ").upper().strip()[0]
# print(f"Você tem o sexo Biológico {sexo}")


# Desafio: Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, entre os palpites diga ao jogador se o número do computador é maior ou menor ao que ele digitou,no final mostre quantos palpites foram necessários para vencer.

import random
from time import sleep

n1 = print(
    "Te proponho um jogo simples, eu penso em um numero e você tenta adivinhar, facil não ?")
sleep(2)
n2 = int(input("Digite o numero que você arrisca ser o correto: "))

x = 0
x = random.randint(1, 10)
m2 = 0


while True:
    if x == n2:
        print(f"Você acertou depois de tentar {m2} vezes")
        break

    else:
        print("Você errou , digite novamente")
        m2 = m2 + 1
        n2 = int(input("Digite o numero que você arrisca ser o correto: "))
        print(x)
