import pandas as pd

class frame:
    def __init__(self):
        self.tabuleiro = {i:0 for i in range(9)}
        print('Bem-vindo ao Jogo da Velha created by Xibs')

    def reiniciar_jogo(self):
        self.tabuleiro = {i:0 for i in range(9)}
    
    def locais_vazios(self):
        self.empty_spc = [i for i,j in self.tabuleiro.items() if j==0]
        return self.empty_spc
    
    def retorna_tabuleiro(self):
        return self.tabuleiro
    
class jogador:
    def __init__(self, tipo, Tabuleiro):
        self.player = tipo
        self.Tabuleiro = Tabuleiro
        print(f'Bem-vindo player {self.player}.')

    def marcar(self, pos):
        tabuleiro_atm = self.Tabuleiro.retorna_tabuleiro()
        self.Tabuleiro.tabuleiro[pos] = self.player
        print(tabuleiro_atm)



Tabuleiro = frame()
player_x = jogador('X', Tabuleiro)
player_o = jogador('O', Tabuleiro)

jogo = 0
i = 1

while jogo != 1:
    jogada = int(input(f'Em qual das posições deseja jogar? {Tabuleiro.locais_vazios()}'))
    if i % 2 == 0:
        player_x.marcar(jogada)
    else:
        player_o.marcar(jogada)

    if Tabuleiro.locais_vazios() == []:
        jogo = 1
    else:
        i += 1


        