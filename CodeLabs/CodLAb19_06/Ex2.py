# 01 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
import os


class Jogador:

    def __init__(self, nome, partidas=0, gols=0):
        self.nomeJogador = nome
        self.partidasJogador = partidas
        self.golsJogador = gols

    def mostrarJogador(self):
        totalGols = self.golsJogador * self.partidasJogador
        return f'''
        O jogador{self.nomeJogador}
        Teve {self.partidasJogador} partidas
        Gols {self.golsJogador} por partida
        Total de {totalGols} Gols por partida

        '''


os.system("cls")
cadastrarJogador = Jogador(
    str(input("Qual o nome do Jogador: ")).capitalize(),
    int(input("Quantas partidas ele jogou esse ano ?: ")),
    int(input("Quantos gols ele fez por partida ? "))

)
print(cadastrarJogador.mostrarJogador())
