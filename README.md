# 🎮 Jogo da Velha em Python (Terminal)

Este é um jogo da velha simples, interativo e totalmente funcional, feito em Python utilizando classes e NumPy para gerenciamento do tabuleiro.

Criado por **Fernando Santos (aka Xibs)** 🧠🚀

---

## 📌 Como funciona

O jogo é executado no terminal e permite que dois jogadores joguem alternadamente (`X` e `O`) até que:

- Um jogador vença (linha, coluna ou diagonal),
- Ou todas as casas sejam preenchidas (empate).

---

## 🛠️ Tecnologias utilizadas

- Python
- Biblioteca NumPy

---

## 📂 Estrutura do projeto

- `class jogo`: Gerencia o tabuleiro, lógica de vitória, locais disponíveis e reinício.
- `class jogador`: Responsável por marcar uma posição no tabuleiro.
- `main loop`: Alterna entre os jogadores, recebe entrada do usuário e verifica fim de jogo.

---

## 🧠 Lógica do tabuleiro

- O tabuleiro é um `np.array` 3×3, preenchido inicialmente com os números de 1 a 9.
- Cada número representa uma casa livre.
- O jogador escolhe onde marcar com base nesses números.

Tabuleiro inicial:

['1' '2' '3']
['4' '5' '6']
['7' '8' '9']

 
## 💡 Melhorias futuras (ideias)

- Interface gráfica com Tkinter ou PyGame
- Jogo contra o computador (modo IA)
- Pontuação acumulativa entre partidas
