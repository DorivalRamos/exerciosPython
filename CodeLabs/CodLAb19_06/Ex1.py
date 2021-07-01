# Utilizando
# os conceitos de Orientação a Objetos ( vistos na aula
# anterior, crie um lançador de dados e moedas em que o usuário deve
# escolher o objeto a ser lançado Não esqueça que os lançamentos são
# feitos de forma randômica

from random import choice, randint


class Dados:
    def __init__(self, jogo):
        self.game = jogo

    def jogarMoeda(self):
        moeda = ['par', 'impar']
        moedaJogada = choice(moeda)
        return moedaJogada

    def JogarDado(self):
        dado = [1, 2, 3, 4, 5, 6]
        dadoRolado = choice(dado)
        return dadoRolado


jogador = Dados(
    print(input('''Qual jogo você deseja jogar ?
            [1]Moeda
            [2]Dado de 6 lados
      '''))

)
if jogador == 2:
    print(jogador.jogarMoeda())
else:
    print(jogador.JogarDado())
