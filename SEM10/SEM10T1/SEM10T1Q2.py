from random import randrange as rg


def e_par(n: int = int):
    return 'par' if n % 2 == 0 else 'ímpar'


def __main__():
    n = 100
    s = 1
    soma_mais_um_par = 0
    soma_mais_um_impar = 0
    par = 0
    impar = 0
    for i in range(1, n, s):
        entrada = rg(1, 2000000)
        if 'par' == e_par(entrada):
            soma_mais_um_par += 1
        elif 'ímpar' == e_par(entrada):
            soma_mais_um_impar += 1
    par = soma_mais_um_par
    impar = soma_mais_um_impar
    return par, impar


print(__main__())
