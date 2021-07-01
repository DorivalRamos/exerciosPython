class Conta:
    def __init__(self, titular, saldo=10):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        if self.saldo == 0:
            return f'''
                  Titular: {self.titular}
                  '''
        else:
            return f'''
                  Titular: {self.titular}
                  Saldo: {self.saldo}
                  '''

    def depositar(self, valor):
        self.saldo += valor
        return f'{self.titular}seu saldo atual é {self.saldo}'

    def sacar(self, valor):
        if valor > 0:
            if self.saldo <= 0 or self.saldo < valor:
                print('Saldo insuficiente para realizar a ação!!!')
                self.extrato()
            else:
                self.saldo -= valor
                print(f"voçê sacou R${valor:.2f} com sucesso!!")
                self.extrato()
        else:
            print('Você não pode sacar ZERO reais')

    def extrato(self):
        return f'Saldo: R${self.saldo}'
