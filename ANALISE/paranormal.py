from random import *
##import random
##random.seed()
##n = random.randrange(20) + 1
##print(n)
def adivinha_numero():
    seed()
    input('Pense em um número de 1 a 20. ENTER para continuar...')
    n = randrange(20) + 1
    resultado = 0

    x = randrange(2, 10)
    input(f'Some o número com {x}. ENTER para continuar...')
    resultado = n + x
    x = randrange(5, 14)
    input(f'Some o resultado com {x}. ENTER para continuar...')
    resultado = resultado + x

    input('Diminua do resultado o primeiro número que pensou. ENTER para continuar...')
    resultado = resultado - n

    x = randrange(2, 6)
    input(f'Multiplique o resultado pro {x}. ENTER para continuar...')
    resultado = resultado * x

    print(f'O resultado foi {resultado}')


def main():
    adivinha_numero()

if __name__=='__main__':
    adivinha_numero()
