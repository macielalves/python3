def soma_lista(lista):
    soma = 0
    for indices in range(len(lista)):
        soma += lista[indices]

    return soma


def soma_cumulativa(lista):
    lista_soma = []
    lista_auxiliar = []
    for a in lista:
        lista_auxiliar.append(a)
        lista_soma.append(soma_lista(lista_auxiliar))

    return lista_soma


def main():
    lista = []

    # Entrada de dados
    while True:
        n = int(input())
        if n == 0:
            break

        lista.append(n)

    # Processar lista
    valor_soma = soma_cumulativa(lista)

    # Saída
    print(valor_soma)
    pass


if __name__ == "__main__":
    main()
