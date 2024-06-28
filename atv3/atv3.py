
"""
[01:18, 21/06/2024] Cordeiro: GRUPO 3
🚀 [Desafio 002] Desenvolvimento de um Jogo de Adivinhação

O objetivo deste desafio é criar um jogo de adivinhação em que o usuário tentará adivinhar um número gerado aleatoriamente. Siga as especificações abaixo para completar o desafio:

1. Funcionalidades do Jogo:
    - Ao iniciar, o jogo perguntará ao usuário quantas vezes ele deseja jogar e repetirá os sorteios na quantidade informada pelo usuário.
    - Para cada rodada, o jogo pedirá ao usuário para digitar um número entre 1 e 10.
    - O jogo utilizará uma função para gerar um número aleatório de 1 a 10 (função de geração de número randômico).
    - Se o usuário acertar o número, o jogo informará que ele acertou.
    - Se o usuário errar, o jogo informará o número sorteado.
    - A cada repetição do sorteio, caso o usuário tenha acertado, o jogo somará 3 pontos. Se errar, subtrairá 1 ponto.

2. Pontuação Final:
    - No final de todas as rodadas, o jogo apresentará a pontuação final do usuário.

3. Execução do Jogo:
    - O jogo funcionará no terminal, sem necessidade de interface gráfica.

[Desafio 003] O objetivo desta missão e refazer o jogo anterior com uma interface gráfica:

0. A biblioteca para criação da interface é de sua escolha.
"""
import tkinter as tk
from tkinter import messagebox
import random

class JogoAdivinhacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Adivinhação!!")

        self.rodadas = 0
        self.pontuacao = 0
        self.rodada_atual = 0

        self.label_inicial = tk.Label(root, text="Quantas vezes você qr jogar?")
        self.label_inicial.pack()

        self.entry_rodadas = tk.Entry(root)
        self.entry_rodadas.pack()

        self.botao_iniciar = tk.Button(root, text="Iniciar Jogo", command=self.iniciar_jogo)
        self.botao_iniciar.pack()

        self.label_rodada = tk.Label(root, text="")
        self.label_rodada.pack()

        self.entry_numero = tk.Entry(root)
        self.entry_numero.pack()

        self.botao_adivinhar = tk.Button(root, text="Adivinhar", command=self.adivinhar, state=tk.DISABLED)
        self.botao_adivinhar.pack()

        self.label_resultado = tk.Label(root, text="")
        self.label_resultado.pack()

        self.label_pontuacao = tk.Label(root, text="")
        self.label_pontuacao.pack()

    def iniciar_jogo(self):
        try:
            self.rodadas = int(self.entry_rodadas.get())
            if self.rodadas <= 0:
                raise ValueError
            self.rodada_atual = 0
            self.pontuacao = 0
            self.label_resultado.config(text="")
            self.label_pontuacao.config(text="")
            self.proxima_rodada()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, informa um número válido de rodadas.")

    def proxima_rodada(self):
        self.rodada_atual += 1
        if self.rodada_atual > self.rodadas:
            self.fim_jogo()
        else:
            self.label_rodada.config(text=f"Rodada {self.rodada_atual} de {self.rodadas}")
            self.botao_adivinhar.config(state=tk.NORMAL)
            self.entry_numero.delete(0, tk.END)
            self.entry_numero.focus()

    def adivinhar(self):
        try:
            numero_usuario = int(self.entry_numero.get())
            if numero_usuario < 1 or numero_usuario > 10:
                raise ValueError
            numero_sorteado = random.randint(1, 10)
            if numero_usuario == numero_sorteado:
                self.pontuacao += 3
                self.label_resultado.config(text=f"Você acertou! O número era {numero_sorteado}.")
            else:
                self.pontuacao -= 1
                if self.pontuacao < 0:
                    self.pontuacao = 0  # Evita pontuação negativa
                self.label_resultado.config(text=f"Você errou! O número era {numero_sorteado}.")
            self.label_pontuacao.config(text=f"Pontuação: {self.pontuacao}")
            self.botao_adivinhar.config(state=tk.DISABLED)
            self.root.after(2000, self.proxima_rodada)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, informa um número válido entre 1 e 10.")

    def fim_jogo(self):
        messagebox.showinfo("Fim de Jogo", f"Fim de jogo! Sua pontuação final é {self.pontuacao}.")
        self.label_rodada.config(text="")
        self.label_resultado.config(text="")
        self.label_pontuacao.config(text="")
        self.entry_rodadas.delete(0, tk.END)
        self.entry_numero.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoAdivinhacao(root)
    root.mainloop()
