class Conta:
    def __init__(self, titular, saldo=10):
        self.titular = titular
        self.__saldo = saldo

    def __str__(self):
        if self.__saldo == 0:
            return f'''
                  Titular: {self.titular}
                  '''
        else:
            return f'''
                  Titular: {self.titular}
                  Saldo: {self.__saldo}
                  '''

    def depositar(self, valor):
        self.__saldo += valor
        return f'{self.titular}seu saldo atual é {self.__saldo}'

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo <= 0 or self.__saldo < valor:
                print('Saldo insuficiente para realizar a ação!!!')
                self.extrato()
            else:
                self.__saldo -= valor
                print(f"voçê sacou R${valor:.2f} com sucesso!!")
                self.extrato()
        else:
            print('Você não pode sacar ZERO reais')

    def extrato(self):
        return f'Saldo: R${self.__saldo}'
