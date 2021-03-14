def computador_escolhe_jogada(n, m):
    computador = True
    i = 1
    while (i <= m and i <= n):
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
        print("Ops... Número de peças inválido! Tente novamente.")
        pecas_retiradas = int(input(Insira o nº de peças que você deseja retirar:))
    return pecas_retiradas


def partida():
    computador = False
    usuario = False

    n = int(input("Defina o número de peças por jogada: "))
    m = int(input("Defina o limite do número de peças por jogada: "))

def campeonato():
    pass