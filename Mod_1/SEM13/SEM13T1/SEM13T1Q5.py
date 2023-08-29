def intercala_lista(lista1, lista2, length):
    lista3 = []
    for i in range(length):
        lista3.append(lista1[i])
        lista3.append(lista2[i])

    return lista3


def main():
    l1 = []
    l2 = []
    length = 25
    for lista in range(length):
        l1.append(int(input('Digite um número: ')))

    for lista in range(length):
        l2.append(int(input('Digite um número: ')))

    lista3 = intercala_lista(l1, l2, length)
    print(l1)
    print(l2)
    print(lista3)


if __name__ == "__main__":
    main()
