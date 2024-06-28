'''
GRUPO 3
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
    - O jogo funcionará no terminal, sem necessidade de interface gráfica.
'''

import random #bibioteca pra gerar números aleatórios.

# Pergunta quantas vezes ele qr jogarr
num_rod = int(input("Quantas vezes você qr jogar? "))

if num_rod == 0:
    print(f"\nO numero rodadas não pode ser {num_rod}")
else:
    # Inicializa a pontuação do usuário
    pontuacao = 0

    # Loop para cada uma rodada do jogo
    for rodada in range(num_rod):
        print(f"\nRodada {rodada + 1}/{num_rod}")

        # Pede um número entre 1 e 10
        resp = int(input("Digite um número entre 1 e 10: "))

        # Gera um número aleatório entre 1 e 10
        num_aleatorio = random.randint(1, 10)

        # Verifica se o a resposta está correto
        if resp == num_aleatorio:
            print("Você acertou!")
            # Se o usuário acertar, soma 3 pontos
            pontuacao += 3
        else:
            print(f"Você errou! O número correto foi {num_aleatorio}.")
            # Se errar, -1 ponto
            pontuacao -= 1

    # Exibe a pontuação final
    print(f"\nSua pontuação final é: {pontuacao}")
