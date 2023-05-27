def lista_numeros():
    lista = []
    par = []
    impar = []

    for i in range(20):
        try:
            numero = int(input())
        except ValueError:
            continue
        else:
            lista.append(numero)
            if numero % 2 == 0:
                par.append(numero)
            else:
                impar.append(numero)
    return lista, par, impar


def main():
    lista, par, impar = lista_numeros()
    print(lista)
    print(par)
    print(impar)


if __name__ == "__main__":
    main()
