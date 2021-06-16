
# #01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

# min = int(1000)
# max = int()
# for c in range(1, 4):
#     p1 = int(input(f"Digite o peso da {c}°: "))
#     if p1 > max:
#         max = p1
#     if p1 < min:
#         min = p1
# print(f"O maior peso foi {max}, o menor peso foi {min} ")


# 02 - Crie um programa que pergunte ao usuário um número inteiro e faça a tabuada desse número.
# from time import sleep
# n1 = int(input("Digite o numero para receber a taboada: "))
# print(f"A taboada do numero{n1}")
# for c in range(1, 11):
#     sleep(1)
#     print(f"{n1} * {c} = {n1 * c}")


# 03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final,mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

# from datetime import datetime
# ano = datetime.today().year

# menor = int()
# maior = int()
# for con in range(0, 5):
#     p1 = int(input("Digite o ano de nascimento: "))
#     if (ano - p1) < 18:
#         menor = menor + 1
#     else:
#         maior = maior + 1
# print(f"{maior} Pesoas são de Maioresa\n {menor} Pessoas de Menores")

# 04 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.Mostre também quantos valores pares foram digitados.


# n = 0
# for c in range(0, 6):
#     n1 = int(
#         input(f"Digite {6 - c} numeros para ser feita a soma deles, apénas os pares: "))

#     if n1 % 2 == 0:
#         n = n + n1
# print(f"A soma dos numeros pares foi {n}")
