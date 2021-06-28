# 4. Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

from random import randint


def salario_func():
    salario = randint(1000, 5000)
    horasT = randint(0, 100)
    if horasT >= 40:
        return f'''
     O seu Salario é de R${salario}
      com {horasT} Horas trabalhadas então você receberá {salario * 1.5}
    '''
    else:
        return f'''
    O seu Salario é de R${salario}
      com {horasT} Horas trabalhadas então você receberá {salario}
    '''


print(salario_func())
