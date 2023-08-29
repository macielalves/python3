# 1º ler uma matriz MxM, ordem n, e n deve ser digitado pelo usuário, sendo n>0 e inteiro
# 2º processar a matriz coletando a posição do menor e maior elemento da matriz
# 3º os valores processados devem ter saída do tipo tupla(linha, coluna) da posição de cada elemento

def maior_da_matriz(matriz: list):
    maior = matriz[0][0]  # para uma matriz quadrada homogênea
    l_maior, c_maior = 0, 0
    for lin in range(len(matriz)):
        for col in range(len(matriz[lin])):
            aux = matriz[lin][col]
            if aux > maior:
                maior, l_maior, c_maior = aux, lin, col

    return l_maior, c_maior


def menor_da_matriz(matriz: list or tuple):
    menor = matriz[0][0]  # para uma matriz quadrada homogênea
    l_menor, c_menor = 0, 0  # referente ao valor inicial
    for lin in range(len(matriz)):
        for col in range(len(matriz[lin])):
            aux = matriz[lin][col]
            if aux < menor:
                menor, l_menor, c_menor = aux, lin, col

    return l_menor, c_menor


def main():
    matriz = []
    ordem = abs(int(input('Digite a ordem da matriz: ')))  # Ordem da matriz quadrada
    for lin in range(ordem):
        linha = []
        for col in range(ordem):
            linha.append(int(input(f"{lin, col} Insira um valor na matriz: ")))

        matriz.append(linha)

    print(f"O maior valor da matriz está na posição {maior_da_matriz(matriz)}")
    print(f"e o menor está na posição {menor_da_matriz(matriz)}")


if __name__ == "__main__":
    main()
