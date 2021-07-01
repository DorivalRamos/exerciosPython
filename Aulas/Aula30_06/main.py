import sys
from conta import Conta
from random import randint
import os

banco = list()
# for o in banco:
# print(0)

if __name__ == '__main__':
    while True:
        conta = Conta(
            titular='Dorival'  # input('Titular: ')
        )

        banco.append(conta)

        ação = input('''
        Qual operação deseja realizar ?
        [1]Depositar
        [2]Sacar
        [3]extrato

    ''')

        resp = input('Deseja continuar? [S/N]?').upper().strip()[0]

        if resp == 'N':
            os.system('cls')
            break


for c in banco:
    c.depositar(
        float(input(f'{c.titular} quanto você deseja depositar? R$ ')))
    c.sacar(float(input(f'{c.titular} quanto você deseja sacar? R$ ')))

    # Fazer o método sacar(), se o saldo for menor ou igual a 0, retorne uma mensagem dizendo que o saldo é insuficiente, caso o contrário, realize a operação de saque e mostre o saldo atual dessa conta;
