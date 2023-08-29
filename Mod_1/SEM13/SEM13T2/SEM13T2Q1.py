def multiplica_contanste(lista, constante):
    mult = []
    for i in lista:
        mult.append(i * constante)

    return mult


def main():
    lista = []
    while True:
        numero = int(input('Digite um número: '))
        if numero == 0:
            break
        else:
            lista.append(numero)

    k = int(input('Digite um numero para ser o multiplicador: '))
    multiplicados = multiplica_contanste(lista, k)
    print(multiplicados)


if __name__ == "__main__":
    main()
