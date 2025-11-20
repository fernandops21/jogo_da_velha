import pandas as pd
import numpy as np

class jogo:
    def __init__(self):
        self.tabuleiro = np.array([str(i) for i in range(1,10)]).reshape(3, 3)
        print('Bem-vindo ao Jogo da Velha created by Xibs.\n')
    
    def retorna_mapa(self):
        self.map_tabuleiro = {valor:(i,j) for (i,j),valor in np.ndenumerate(self.tabuleiro)}
        return self.map_tabuleiro

    def reiniciar_jogo(self):
        self.tabuleiro = np.array([i for i in range(1,10)]).reshape(3, 3)
    
    def locais_vazios(self):
        self.empty_spc = [valor for (i,j),valor in np.ndenumerate(self.tabuleiro) if ((valor != 'X') and (valor != 'O'))]
        return self.empty_spc
    
    def retorna_tabuleiro(self):
        print(self.tabuleiro)
        return self.tabuleiro
    
    def check_fim_de_jogo(self):
        self.jogo = 0
        check_linha = any([(len(set(self.tabuleiro[i]))==1) for i in range(3)])
        check_coluna = any([(len(set(self.tabuleiro[:,i]))==1) for i in range(3)])
        check_diagonal = len(set(np.diagonal(self.tabuleiro))) == 1
        if check_linha or check_coluna or check_diagonal:
           self.jogo = 1
        return self.jogo
    
class jogador:
    def __init__(self, tipo, Tabuleiro):
        self.player = tipo
        self.Tabuleiro = Tabuleiro
        print(f'Bem-vindo jogador {self.player}.')

    def marcar(self, pos):
        mapa_tabuleiro = self.Tabuleiro.retorna_mapa()
        coord_marcar = mapa_tabuleiro[pos]
        self.Tabuleiro.tabuleiro[coord_marcar] = self.player
        self.Tabuleiro.retorna_tabuleiro()

Tabuleiro = jogo()
player_x = jogador('X', Tabuleiro)
player_o = jogador('O', Tabuleiro)

jogo = Tabuleiro.check_fim_de_jogo()
i = 1

while jogo != 1:
    if i==1:
        Tabuleiro.retorna_tabuleiro()

    if i % 2 != 0:
        print(f'\nPlayer X é sua vez de jogar!')
        jogada = input(f'Onde deseja marcar? {Tabuleiro.locais_vazios()}: ')
        player_x.marcar(jogada)

    else:
        print(f'\nPlayer O é sua vez de jogar!')
        jogada = input(f'Onde deseja marcar? {Tabuleiro.locais_vazios()}: ')
        player_o.marcar(jogada)

    if Tabuleiro.locais_vazios() == []:
        jogo = 1
        print('\nFim de jogo. Empate!')
    else:
        i += 1
        jogo = Tabuleiro.check_fim_de_jogo()

        if jogo == 1:
            if i % 2 != 0:
                print('\nFim de jogo. Parabéns jogador X!')
            else:
                print('\nFim de jogo. Parabéns jogador O!')