import numpy as np

class Jogo:
    def __init__(self):
        self.tabuleiro = np.array([str(i) for i in range(1,10)]).reshape(3, 3)
        print('Bem-vindo ao Jogo da Velha created by Xibs.\n')
    
    def retorna_mapa(self):
        self.map_tabuleiro = {valor:(i,j) for (i,j),valor in np.ndenumerate(self.tabuleiro)}
        return self.map_tabuleiro

    def reiniciar_jogo(self):
        self.tabuleiro = np.array([str(i) for i in range(1,10)]).reshape(3, 3)
    
    def locais_vazios(self):
        self.empty_spc = [valor for (i,j),valor in np.ndenumerate(self.tabuleiro) if ((valor != 'X') and (valor != 'O'))]
        return self.empty_spc
    
    def retorna_tabuleiro(self):
        print(self.tabuleiro)
        return self.tabuleiro
    
    def check_fim_de_jogo(self):
        self.jogo = 0
        diag_princ = self.tabuleiro.diagonal()
        diag_sec = np.fliplr(self.tabuleiro).diagonal()
        check_linha = any([(len(set(self.tabuleiro[i]))==1) for i in range(3)])
        check_coluna = any([(len(set(self.tabuleiro[:,i]))==1) for i in range(3)])
        check_diagonal = (len(set(diag_princ)) == 1 or len(set(diag_sec)) == 1)
        check_spc = self.locais_vazios() == []

        if check_linha or check_coluna or check_diagonal or check_spc:
           self.jogo = 1
        return self.jogo
    
class Jogador:
    def __init__(self, tipo, Jogo):
        self.player = tipo
        self.Jogo = Jogo
        print(f'Bem-vindo jogador {self.player}.')

    def marcar(self, pos):
        mapa_tabuleiro = self.Jogo.retorna_mapa()
        coord_marcar = mapa_tabuleiro[pos]
        self.Jogo.tabuleiro[coord_marcar] = self.player
        self.Jogo.retorna_tabuleiro()

tabuleiro = Jogo()
player_x = Jogador('X', tabuleiro)
player_o = Jogador('O', tabuleiro)

jogo = tabuleiro.check_fim_de_jogo()
i = 1

while jogo != 1:
    invalido = True

    if i==1:
        tabuleiro.retorna_tabuleiro()

    if i % 2 != 0:
        print(f'\nPlayer X é sua vez de jogar!')
        while invalido:
            jogada = input(f'Onde deseja marcar? {tabuleiro.locais_vazios()}: ')
            if jogada in tabuleiro.locais_vazios():
                invalido = False
            else:
                print('Jogada Inválida')

        player_x.marcar(jogada)

    else:
        print(f'\nPlayer O é sua vez de jogar!')
        while invalido:
            jogada = input(f'Onde deseja marcar? {tabuleiro.locais_vazios()}: ')
            if jogada in tabuleiro.locais_vazios():
                invalido = False
            else:
                print('Jogada Inválida')

        player_o.marcar(jogada)
    
    jogo = tabuleiro.check_fim_de_jogo()

    if jogo == 1:
        if tabuleiro.locais_vazios() == []:
            print('\nFim de jogo. Empate!')
        elif i % 2 != 0:
            print('\nFim de jogo. Parabéns jogador X!')
        else:
            print('\nFim de jogo. Parabéns jogador O!')

        reset = '0'
        while (reset != '1') and (reset != '2'):
            reset = input('Deseja jogar novamente? 1 para sim 2 para não: ')
            if reset == '1':
                jogo = 0
                i = 1
                tabuleiro.reiniciar_jogo()
                print('\nNovo Jogo Iniciado!')
            elif reset == '2':
                print('Fim de jogo')
            else:
                print('Entrada inválida.')
    else:
        i += 1