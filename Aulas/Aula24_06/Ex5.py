# Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.


def imc_func():
    altura = 1.68
    peso = 75
    imc = (peso / altura) ** 2
    if imc <= 18.5:
        return 'você esta a baixo'
    elif imc >= 24.9:
        return 'Voce esta acima'
    else:
        return 'Voce esta no imc ideal'


print(imc_func())
