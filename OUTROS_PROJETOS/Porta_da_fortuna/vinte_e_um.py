from random import randint, seed


# inicializa o gerador de números aleatórios
seed()

print('''
Vinte e um!
===========
Tente fazer exatamente 21 pontos!
''')

jogando = True
pontos = 0


while jogando:
    # gera um número aleatório
    numero = randint(1, 10)
    pontos += numero
    print("\nSeu próximo número é", numero)
    print("Sua pontuação agora é", pontos)
    # Condição para o usuário continuar ou não somando os números
    print("\nGostaria de somar mais um número? (S/n)")
    # recebe os dados do usuário
    resposta = input().strip()
    # processa a resposta, e se for n ele retorna false fechando o while
    if resposta[0].lower() == 'n':
        jogando = False


print("Sua pontuação final é", pontos)
if pontos == 21:
    print("Parabéns, você VENCEU!!")
else:
    print("Que pena!!")
