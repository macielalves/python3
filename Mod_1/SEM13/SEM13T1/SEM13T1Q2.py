def n_zeros(n=0):
    """Cria uma lista de n zeros"""
    # lista de n numeros
    lista = []
    # preencher com 0
    for i in range(n):
        lista.append(0)

    return lista


def seq_n(n=0):
    """Sequência de n números
    :param n:
    """
    lista = []
    # preencher de 1 até n
    for i in range(n):
        lista.insert(i, i + 1)

    return lista


def main():

    # entrada do valor de n
    n = int(input("Digite um número inteiro: "))
    lista = []

    lista_de_zeros = n_zeros(n)
    lista_de_sequencia_ate_n = seq_n(n)
    print(lista_de_zeros)
    print(lista_de_sequencia_ate_n)

    # preencher com valores lido pelo teclado
    for i in range(n):
        lista.insert(i, int(input(f"Digite um número, {i+1} de {n} números:  ")))

    print(lista)
    # uso do clear() para usar o espaço da lista anterior para novos dados
    lista.clear()

    for i in range(n):
        lista.insert(i, int(input(f"Digite um número, {i+1} de {n} números:  ")))

    # uso do método reverse() para reverter a ordem dos termos
    lista.reverse()
    print(lista)


if __name__ == "__main__":
    main()
