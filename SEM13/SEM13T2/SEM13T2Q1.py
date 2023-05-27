def multiplica_contanste(lista, constante):
    mult = []
    for i in lista:
        mult.append(i * constante)

    return mult


def main():
    lista = []
    while True:
        numero = int(input())
        if numero == 0:
            break
        else:
            lista.append(numero)

    k = int(input())
    multiplicados = multiplica_contanste(lista, k)
    print(multiplicados)


if __name__ == "__main__":
    main()
