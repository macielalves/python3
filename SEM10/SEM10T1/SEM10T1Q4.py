"""Escreva um programa que gere uma sequência de 10 em 10 até 1000"""


def sequencia():
    acumuladora = ''
    for i in range(0, 1000, 10):
        i += 10
        acumuladora += str(i) + (', ' if i != 1000 else '.')

    return acumuladora


x = sequencia()
print(x)
