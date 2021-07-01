# Crie uma classe chamada Conta para simular as operações de uma conta corrente. Sua classe deverá ter os atributos Titular e Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe Conta e teste os atributos e métodos implementados.​ Adicione uma regra no método Sacar, onde o usuário só poderá sacar se o Saldo for maior que zero, caso contrário mostre a mensagem na tela: "Você não tem saldo suficiente para essa operação."

class Conta:
    def __init__(self, titular, saldo=100):
        self.nomeConta = titular
        self.saldoConta = saldo

    def depositar(self, dinheiro):
        self.saldoConta += dinheiro

    def sacar(self):
        if self.saldoConta == 0 or dinheiro > self.saldoConta:
            return f'Você não tem saldo suficiente para essa operação'
        # elif dinheiro > self.saldoConta:
        #     return f'Você não tem saldo suficiente para essa operação'
        else:
            self.saldoConta -= dinheiro
            return f'Você sacou {dinheiro}'

    def mostrar(self):
        return f'''
      Nome : {self.nomeConta}
      Saldo em conta: {self.saldoConta}
      '''


pessoa = Conta('Dorival')
print(pessoa.sacar(50))
print(pessoa.mostrar())
