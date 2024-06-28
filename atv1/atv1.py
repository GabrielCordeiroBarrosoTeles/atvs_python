'''
[Desafio 001] Desenvolvimento de um Script em Python para Contagem com Incremento

O objetivo deste desafio é construir um script em Python que permita ao usuário realizar uma contagem
a partir de um número inicial até um número final, somando um valor de incremento a cada iteração.
Siga as especificações abaixo para completar o desafio:

1. Especificações Gerais:
    - O script deve ser executado via linha de comando e não requer interface gráfica.
    - O usuário deverá fornecer três números como entrada: número inicial, número final e incremento.
    - O script realizará uma contagem a partir do número inicial até o número final, somando o valor do incremento.
'''
n1 = int(input('Informe o valor inicial: '))
n2 = int(input('Informe o valor final: '))
i = int(input('Informe o valor do  incremento: '))

# Caso o valor inicial for menor que o valor final
if n1 < n2:
    while n1 <= n2:
        print(n1)
        n1 += i
# Caso o valor inicial for maior que o valor final
elif n1 > n2:
    while n1 >= n2:
        print(n1)
        n1 -= i
# Caso se os dois valores informados forem iguais
elif n1 == n2:
    print('O valor inicial {} e o valor final {} , são iguais'.format(n1,n2))