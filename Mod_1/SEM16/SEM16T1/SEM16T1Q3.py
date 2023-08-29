# matriz nxm

def soma_linha(matriz, posicao=0):
    s_linha = 0
    for a in matriz[posicao]:
        s_linha += a
    return s_linha


def soma_coluna(matriz, col=0):
    s_coluna = 0
    for b in matriz:
        s_coluna += b[col]
    return s_coluna


def media_matriz(matriz):
    t = s = 0
    for i in matriz:
        for j in i:
            s += j
            t += 1

    return round(s / t, 4)


def menor_da_matriz(matriz):
    menor = None
    for v in matriz:
        for w in v:
            menor = w if menor is None else w if w < menor else menor
    return menor


def maior_da_matriz(matriz):
    maior = None
    for v in matriz:
        for w in v:
            maior = w if maior is None else w if w > maior else maior
    return maior


def main():
    matriz = []
    n = abs(int(input('Defina um número inteiro para quantidade de linhas da matriz: ')))
    m = abs(int(input('Defina um número inteiro para quantidade de colunas da matriz:  ')))

    for lin in range(n):
        linha = []  # gera uma linha nova a cada execução do laço
        for col in range(m):
            num = int(input(f"({lin},{col}) Digite um numero: "))
            # -
            linha.append(num)  # adiciona os valores na coluna
        matriz.append(linha)

    organizador = []
    organizador.append(soma_linha(matriz=matriz))
    organizador.append(soma_coluna(matriz=matriz, col=-1))
    organizador.append(media_matriz(matriz=matriz))
    organizador.append(menor_da_matriz(matriz=matriz))
    organizador.append(maior_da_matriz(matriz=matriz))

    print(tuple(organizador))
    ...


if __name__ == "__main__":
    main()
