import pandas as pd
import numpy as np

class frame:
    def __init__(self):
        self.tabuleiro = np.full((3, 3), ' ', dtype=str)
        print('Bem-vindo ao Jogo da Velha created by Xibs.\n')

    def reiniciar_jogo(self):
        self.tabuleiro = np.full((3, 3), ' ', dtype=str)
    
    def locais_vazios(self):
        self.empty_spc = [(i+1,j+1) for (i,j),valor in np.ndenumerate(self.tabuleiro) if valor == ' ']
        return self.empty_spc
    
    def retorna_tabuleiro(self):
        return self.tabuleiro
    
class jogador:
    def __init__(self, tipo, Tabuleiro):
        self.player = tipo
        self.Tabuleiro = Tabuleiro
        print(f'Bem-vindo jogador {self.player}.')

    def marcar(self, pos):
        tabuleiro_atm = self.Tabuleiro.retorna_tabuleiro()
        self.Tabuleiro.tabuleiro[int(pos[1])-1,int(pos[3])-1] = self.player
        print(tabuleiro_atm)



Tabuleiro = frame()
player_x = jogador('X', Tabuleiro)
player_o = jogador('O', Tabuleiro)

jogo = 0
i = 1

while jogo != 1:

    if i % 2 != 0:
        print(f'\nPlayer X é sua vez de jogar!')
        jogada = input(f'Onde deseja marcar? {Tabuleiro.locais_vazios()}')
        player_x.marcar(jogada)
    else:
        print(f'\nPlayer O é sua vez de jogar!')
        jogada = input(f'Onde deseja marcar? {Tabuleiro.locais_vazios()}')
        player_o.marcar(jogada)

    if Tabuleiro.locais_vazios() == []:
        jogo = 1
    else:
        i += 1       