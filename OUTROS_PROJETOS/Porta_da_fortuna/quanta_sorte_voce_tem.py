from random import *


seed()

tentativas = 0

# definindo a variável que vai receber os pontos
pontos = 0

print('''
      #####################
      # Porta da fortuna! #
      #####################

Existe um super prêmio atrás destas 3 portas!
Adivinhe qual é a porta certa para ganhar o prêmio!
     _____    _____    _____
    |     |  |     |  |     |
    | [1] |  | [2] |  | [3] |
    |    o|  |    o|  |    o|
    |     |  |     |  |     |
    |_____|  |_____|  |_____|
''')

while pontos < 3:
    tentativas += 1
    print("\nTentativa", tentativas, ": Escolha uma porta (1, 2 ou 3): ")

    porta_escolhida = int(input())
    porta_certa = randint(1, 3)

    print("A porta escolhida foi a ", porta_escolhida)
    print("A porta certa é a ", porta_certa)

    if porta_escolhida == porta_certa:
        print("Parabéns!")
        pontos += 1
    else:
        print("Que peninha!")

    print("Sua pontuação atual é", pontos)


print("\n** Você conseguiu! Terminou o jogo em", tentativas, "tentativas **")
