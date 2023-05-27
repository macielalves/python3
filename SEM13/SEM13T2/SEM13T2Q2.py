def e_par(n):
    return n % 2 == 0


def ordena_lista(lista):
    lista.sort()
    return lista


def produto_por_3ou5(lista):
    auxiliar = []
    for x in range(len(lista)):
        auxiliar.append(lista[x] * (3 if e_par(x) else 5))

    return auxiliar


def main():
    lista = []

    # Entrada do usuário
    for i in range(100):
        lista.append(int(input()))

    # Processamento
    lista_ordenada = ordena_lista(lista)
    lista_calculada = produto_por_3ou5(lista_ordenada)

    # Saída
    print(lista_calculada)
    pass


if __name__ == "__main__":
    main()
