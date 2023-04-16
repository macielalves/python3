a = int(input())
b = int(input())
c = int(input())


def menor_diferenca(a=0, b=0, c=0):
    segundo_valor = abs(b - a)
    terceiro_valor = abs(c - a)
    print(segundo_valor if segundo_valor < terceiro_valor else terceiro_valor)


menor_diferenca(a, b, c)
