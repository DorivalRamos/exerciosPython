from os import system               # Limpar o console.
# Sorteia aleatoriamente uma lista de valores com reposição numa amostra.
from random import choices
from time import sleep              # Pausa entre uma linha e outra.


system('cls')   # Inicia limpando a tela.

# Pergunto ao usuário se ele está pronto, assim o jogo não fica automática demais.
continuar = input(
    '\n\n\nQuando vocês estiverem prontos digite "P": ').strip().upper()[0]
# Bloco de while garante que o jogo só avançará se o usuário teclar 'P'.
while continuar != 'P':
    continuar = input(
        'Ainda não estão prontos? Digite "P" quando estiverem prontos: ').strip().upper()[0]
while True:
    system('cls')
    # Pergunta ao usuário quantas rodadas serão feitas.
    rodadas = 5  # int(input('\n\nQuantas rodadas vocês desejam fazer? '))
    while rodadas < 1:  # Bloco de while garante que o usuário digitará um número maior que 0.
        rodadas = int(
            input('Quantidade inválida. Digite um número maior que 0: '))
    system('cls')
    # Variável usada para contar as vitórias de cada um dos 4 jogadores.
    vitorias = [0, 0, 0, 0]
    # Nesse bloco de for serão feitas todas as rodadas pedidas pelo usuário.
    for i in range(rodadas):
        rodada = (f'RODADA#{i+1}')
        # Variável declarada para fazer o efeito de contagem em ASCII Art.
        contagem = ["3...", "2...", "1..."]
        print(f'{rodada}\n')
        sleep(1)
        # Nesse bloco de for será feita a contagem declarada acima, aparecendo cada item um a um.
        for c in contagem:
            print(c)
            sleep(1)
        system('cls')
        # Esse dicionário vai armazenar os dados de cada jogador em cada rodada.
        jogadores = dict()
        # Comando choices gerará 4 números aleatórios entre 1 e 7, exclusive.
        jogadas = choices(range(1, 7), k=4)
        # Nesse bloco de for serão armazenados os valores gerados pelo choices nas chaves do dicionario de cada jogador.
        for j in range(1, 5):
            jogadores[j] = jogadas[j-1]
        print(f'\n"RESULTADO:")\n')
        sleep(1)
        # Nesse bloco de for o dicionário será organizado em ordem decrescente em relação ao valor do dado.
        for index, valor in sorted(jogadores.items(), key=lambda x: x[1], reverse=True):
            # Esse bloco de if e else servirá para adicionar uma unidade aos index dos jogadores com maior valor na variável vitória.
            if valor == max(jogadas):
                vitorias[index-1] += 1
                print(
                    f'+1 PONTO PARA O JOGADOR {index}! O DADO caiu em {valor}.')
            else:  # Se não foi o maior valor, simplesmente mostra na tela.
                print(f'O 🎲 do Jogador {index} caiu em {valor}.')
            sleep(1)

            print(f'"FINAL DE JOGO!"')
            sleep(1.5)
            print('\n\n\nSomando os pontos de todos os jogadores', end='')
            sleep(.5)
            # Esse bloco de for é apenas para aparecer pontinhos na tela, para fazer um suspense.
            for k in '.'*10:
                # Parâmetro flush serve garantir que aparecerá os pontos um após o outro.
                print(k, end='', flush=True)
                sleep(.5)
    system('cls')
    vencedores = list()    # Essa variável armazenará o index de todos os vencedores
    # Bloco de for utilizando o enumerate para comparar o número de vitórias de cada jogador com o max(vitorias) e adiconando seu index à variável 'vencedores '.
    for index, valor in enumerate(vitorias):
        if valor == max(vitorias):
            vencedores.append(index+1)
    # Garantindo o plural na palavra 'vitória', caso seja maior que 1.
    vitoria = '1 vitória' if max(
        vitorias) == 1 else f'{max(vitorias)} vitórias'
    # Bloco de if, elife e else, para mostrar na tela todos os vencedores, independete de quantos tenham sido.
    if len(vencedores) == 1:    # Caso só tenha 1 vencedor.
        print(f'\n                Com {vitoria}, o grande campeão 🏆 é.....\n')
        sleep(2)
        print(f'                  Jogador   {vencedores[0]}')
    elif len(vencedores) == 2:  # Caso tenha 2 vencedores.
        print(
            f'\n                Foi uma partida muuuito acirrada...\nCom {vitoria} cada, os vencedores 🏆 são:\n')
        sleep(2)
        print(
            f'                Jogador   {vencedores[0]}\nJogador   {vencedores[1]}')
    elif len(vencedores) == 3:  # Caso tenha 3 vencedores.
        print(
            f'\n                Foi uma partida muuuito acirrada...\nCom {vitoria} cada, os vencedores 🏆 são:\n')
        sleep(2)
        print(
            f'                  Jogador   {vencedores[0]}\nJogador   {vencedores[1]}\nJogador   {vencedores[2]}')
    else:   # Caso tenha 4 vencedores.
        print(
            f'\n                Essa foi uma partida incrível!!!\nCom {vitoria} cada, os 4 jogadores......\n')
        sleep(2)
        print('                 EMPATARAM!')
    continuar = input(
        '\n\n\nDeseja jogar novamente? [S/N] ').strip().upper()[0]
    # Bloco de while garante que o usuário teclará "S" ou "N".
    while continuar not in 'SN':
        continuar = input(
            'Comando inválido. Digite novamente: [S/N] ').strip().upper()[0]
    # Se teclar "N", o programa agradece, limpa a tela e finaliza.
    if continuar == 'N':
        sleep(1)
        print('\n\nObrigado por jogar!')
        sleep(3)
        system('cls')
        break
    system('cls')
