G = '\033[32m'
Y = '\033[33m'
N = '\033[0m'
cor1 = Y
cor2 = G
valor = float(input(f'Informe um preço: '))
porcent = float(input(f'Informe a porcentagem: '))

def acrescimo(v, p):
    pvalor = v * p / 100
    return v + pvalor

def decrescimo(v, p):
    pvalor = v * p / 100
    return v - pvalor

print(f'O valor com acréscimo é {cor2}{acrescimo(valor, porcent):.2f}{N}')
print(f'O preço com desconto é {cor2}{decrescimo(valor,porcent):.2f}{N}')
