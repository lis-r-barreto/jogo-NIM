def jogar():
    modalidade_jogo = 0
    while (modalidade_jogo != 1 and modalidade_jogo != 2):
           modalidade_jogo = int(input("""Seja bem-vindo ao jogo do NIM! Escolha a modalidade de jogo:
                  [1] Partida Isolada
                  [2] Campeonato\n"""))
    if (modalidade_jogo == 1):
            print ("Voce escolheu uma partida isolada!")
            partida()
    elif (modalidade_jogo == 2):
           print ("Voce escolheu um campeonato!")
           campeonato()

def computador_escolhe_jogada(n, m):
    computador = True
    for i in range (1 , m):
        if ((n - i) % (m + 1) == 0):
            return i
        else:
            i = i + 1
    if m <= n:
        return m

def usuario_escolhe_jogada(n, m):
    usuario = True
    pecas_retiradas = int(input(Insira o nº de peças que você deseja retirar:))
    while ((pecas_retiradas > maximo_peças) or (pecas_retiradas <= 0)):
        print("Ops... Nº de peças inválido! Tente novamente.")
        pecas_retiradas = int(input(Insira o nº de peças que você deseja retirar:))
    return pecas_retiradas

def partida():
    computador = False
    usuario = False

    n = int(input("Defina o número de peças por jogada: "))
    m = int(input("Defina o limite do número de peças por jogada: "))

def campeonato():
    pass

vitorias_jogador = 0
vitorias_computador = 0
jogar()