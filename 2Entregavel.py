from random import randint
from time import sleep

itens = ("Papel", "Pedra", "Tesoura")
computador = randint(0, 2)
tentativas = int()

pergunta = int(
    input("Vamos jogar JO KE PO?, me diga quantas vezes você vai me desafiar ?: "))
sleep(1)
for c in range(pergunta):
    print("-=" * 12)
    jogador = int(input('''Qual você escolhe?\n
 [0]Papel\n
 [1]Pedra\n
 [2]Tesoura\n'''))
    print("-=" * 12)
    print(f"O computador escolheu {itens[computador]}")
    print(f"Você escolheu {itens[jogador]}")
    sleep(1)

    if computador == 0:
        if jogador == 0:  # Jogador escolheu Papel
            print("Empate")
        elif jogador == 1:  # Jogador escolheu Pedra
            print("Você perdeu!!!")
        elif jogador == 2:  # Jogador escolheu Tesoura
            print("Você ganhou !!!")
            tentativas += 1

    if computador == 1:
        if jogador == 0:  # Jogador escolheu Papel
            print("Você ganhou")
            tentativas += 1
        elif jogador == 1:  # Jogador escolheu Pedra
            print("Você empatou!!!")
        elif jogador == 2:  # Jogador escolheu Tesoura
            print("Você perdeu !!!")

    if computador == 2:
        if jogador == 0:  # Jogador escolheu Papel
            print("Você Perdeu")
        elif jogador == 1:  # Jogador escolheu Pedra
            print("Você Ganhou!!!")
            tentativas += 1
        elif jogador == 2:  # Jogador escolheu Tesoura
            print("Você Empatou !!!")

print(f"Você ganhou {tentativas} Vezes!!")
