from time import *
# Althor: Maciel Alves Pereira
# qs1 possui dados retirados de www.acervolima.com
# não executar no shell python, pode ser que ainda não tenha suporte as cores

#cor de fundo
verde = '\033[7;92m'
vermelho = '\033[7;91m'
amarelo = '\033[7;93m'
branco = '\033[7;99m'
#cor da letra
o = '\033[0;35m'
v = '\033[3;32m'
m = '\033[2;93m'
z = '\033[1;36m'
l = '\033[0;m'


def main():
    global velocidade
    velocidade = 2
    score = 0
    if input(f'{branco} Você gostaria de participar deste quiz?[1]Sim [2]Não:{l} ').strip().lower() in ('1', 's', 'sim'):
        print('{:^50}'.format(f'{z} A qui vai a primeira pergunta: {l}'))
        sleep(velocidade - velocidade // 2)

        if qs1() == 1:
            score += 1
        sleep(velocidade)

        if qs2() == 1:
            score += 1
        sleep(velocidade)

        if qs3() == 1:
            score += 1
        sleep(velocidade)

        if qs4() == 1:
            score += 1
        sleep(velocidade)

        if qs5() == 1:
            score += 1
        sleep(velocidade)

        if score == 5:
            if input('Você aceita uma questão bônus?[S/n]: ').strip().lower() in ('sim', 's', 'y', 'yes'):
                if qs6() == 1:
                    score += 5
                    sleep(velocidade)
                    
                if score == 10:
                    print(f"{branco}Parabéns, voçê é fera!{l}")
                print(f'{branco}Parabéns por acertar todas as perguntas!{l}')
                print(f'{branco}Você conquistou {amarelo}%d{l}{branco} pontos{l}' % score)
            else:
                print(f'{branco} Parabéns por acertar todas essas perguntas! {l}')
                print(f'{branco} Você conquistou %d pontos {l}' % score)

        else:
            print(f'{branco} Você conquistou %d pontos {l}' % score)

        sleep(velocidade)



def qs1():
    
    ponto = 0
    q1 = input(f'''
(1) No meio tecnológico, o que é python?
[{v}a{l}] Cobra
[{v}b{l}] Linguagem de Programação
Resposta: \
''').strip()

    if q1 == 'a':
        print(f'{vermelho} Resposta errada! {l}\n')

    elif q1 == 'b':
        print(f'{verde} Certa resposta! {l}\n')
        ponto = 1

    elif q1 == 'q':
        return sair()

    else:
        msg()
        sleep(5)
        return qs1()

    print(f'''
{amarelo}
          Python é uma linguagem de programação de alto nível de uso geral amplamente usada.             
Foi criado por Guido van Rossum em 1991 e posteriormente desenvolvido pela Python Software Foundation... {l}\n
''')
    return ponto

def qs2():
    ponto = 0
    q2 = input(f'''
(2) No Python, como se chama uma "caixa" usada para armazenar dados?
[{v}a{l}] texto
[{v}b{l}] variavel
[{v}c{l}] uma caixa de sapatos
Resposta: \
''').strip()
    
    if q2 == 'a':
        print(f'{vermelho} Não - texto é um tipo de dado:( {l}')

    elif q2 == 'b':
        print(f'{verde} Correto!! :) {l}')
        ponto += 1

    elif q2 == 'c':
        print(f'{vermelho} Não exatamente :( {l}')

    elif q2 == 'q':
        return sair()

    else:
        msg()
        sleep(5)
        return qs2()
    return ponto

def qs3():
    
    ponto = 0
    q3 = input(f'''
(3) Qual palavra inicia-se a criação de uma função(modulo) python?
[{v}a{l}] float
[{v}b{l}] int
[{v}c{l}] function
[{v}d{l}] def
Resposta: \
''').strip()
    
    if q3 == 'a':
        print(f'{vermelho} float - é um tipo de dado :( {l}')

    elif q3 == 'b':
        print(f'{vermelho} int - é um tipo de dado  :( {l}')

    elif q3 == 'c':
        print(f'{vermelho} function - é intuitivo mas não é essa a resposta correta! :( {l}')

    elif q3 == 'd':
        print(f'{verde} Certa resposta {l}')
        ponto += 1

    elif q3 == 'q':
        return sair()
    else:
        msg()
        sleep(5)
        return qs3()
    
    return ponto

def qs4():
    
    ponto = 0
    q4 = input(f'''
(3) Qual será a saída do código:
                                    
{m}def{l} {z}main(){l}:
    {v}print{l}('Hello World!'.lower())
{m}if{l} __name__ {o}=={l} '__main__':
    main()

# opções:
[{v}a{l}] hello world!
[{v}b{l}] HELLO WORLD!
[{v}c{l}] Hello World!

Resposta:\
''').strip()
    
    if q4 == 'a':
        print(f'{verde} Certa resposta :) {l}')
        ponto += 1

    elif q4 == 'b':
        print(f'{vermelho} Não, este formato é gerado com o código print("Hello World!".upper()) dentro do módulo main. {l}')

    elif q4 == 'c':
        print(f'{vermelho} Não, este formato é gerado com o código print("Hello World!".title()) dentro do módulo main. {l}')

    elif q4 == 'q':
        return sair()
    else:
        msg()
        sleep(5)
        return qs4()

    return ponto

def qs5():
    ponto = 0
    q5 = input(f'''
(5) Qual a saída do código:
{z}x{l} = {o}min{l}(5, 10, 25)
{z}y{l} = {o}max{l}(5, 10, 25)
{v}print{l}(x, y)

[{v}a{l}] 10, 25
[{v}b{l}] 5, 10
[{v}c{l}] 5, 25
Resposta:\
''').strip()
    if q5 == 'a':
        print(f'{vermelho} Não, somente o valor 25 está correto :( {l}')
        ponto += 1

    elif q5 == 'b':
        print(f'{vermelho} Não, somente o valor 5 está correto! :( {l}')

    elif q5 == 'c':
        print(f'{verde} Certa resposta :) {l}')
        ponto += 1

    elif q5 == 'q':
        return sair()
    else:
        msg()
        sleep(5)
        return qs5()

    return ponto

def qs6():
    
    ponto = 0
    q6 = input(f'''
(6) Bônus, valendo {o}5{l} pontos
Qual a saída:

{v}print{l}('    M$ciel/$lves0000'.replace('$', 'a').replace('/', ' ').title().strip().rstrip('0'))

[{v}a{l}] Maciel/Alves
[{v}b{l}] Maciel Alves
[{v}c{l}] M$ciel/$lves0000
[{v}d{l}] Erro

Resposta:\
''').strip()
    
    if q6 == 'a':
        print(f'{vermelho} Errada {l}')
        ponto += 1

    elif q6 == 'b':
        print(f'{verde} Correta {l}\n')
        ponto += 1

    elif q6 == 'c':
        print(f'{vermelho} Errada {l}')
    elif q6 == 'd':
        print(f'{m} Ela foi testa da na versão python 3.10 e não retornou erro. {l}')

    elif q6 == 'q':
        return sair()
    else:
        msg()
        sleep(5)
        return qs6()

    return ponto

def msg():
    print(f'{branco} Digite [q] na parte de resposta para sair ou responda com uma das opções ente []. {l}')

def sair():
    return quit()


if __name__ == '__main__':
    main()
