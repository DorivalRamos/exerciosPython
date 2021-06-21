# #01 - Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while
# sem break)


# from time import sleep
# n = int(0)
# print("Este programa é uma calculadora simples, você devera digitar dois valores e selecinar qual operaçã deseja fazer ")
# while n == 0:
#     res = int()

#     sleep(1)
#     n1 = float(input("Digite o primero numero: "))
#     sleep(1)
#     n2 = float(input("Digite o segundo numero: "))
#     n3 = int(input('''
#               [ 1 ] somar
#               [ 2 ] multiplicar
#               [ 3 ] maior
#               [ 4 ] novos números
#               [ 5 ] sair do programa
# : '''))
#     if n3 == 1:
#         res += n1 + n2
#         print(f"A soma de {n1} + {n2} = {res}")

#     elif n3 == 2:
#         res += n1 * n2
#         print(f"A Multiplicação de {n1} * {n2} = {res}")

#     if n3 == 3:
#         if n1 == n2:
#             print("São iguais")
#         elif n1 > n2:
#             print(f"{n1} maior que {n2}")
#         else:
#             print(f"{n2} maior que {n1} ")

#     if n3 == 5:
#         n = n + 1


# 02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

from time import sleep
print("Por favor digite seu Sexo [M/F] e sua idade e no final eu irei mostrar Quantas foras as maiores de idade, quantos  eram homens e quantas mulheres tem menos de 20 anos")

while True:
    n1 = int()
    n2 = int()
    n3 = int()
    p1 = str(input("Qual o seu sexo: ").upper().split()[0])
    sleep(2)
    p2 = int(input("Qual a sua idade?: ")).upper().split()
    sleep(2)
    p3 = str(input("Deseja continuar ?[S/N]: ")).upper().split()

    if p2 > 18:
        n1 = n1 + 1
    if p1 == 'M':
        n2 = n2 + 1
    if p1 == 'F' and p2 < 20:
        n3 = n3 + 1

    if p3 == 'N':
        print(f'''
        {n1} Pessoas tem mais de 18 anos de idade\n
        {n2} Homens foram cadastrados\n
        {n3} Mulheres com mais de 18 anos de idade
      ''')
