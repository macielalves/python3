def esta_ordenado(lista):
    for i in range(len(lista)):
        if type(lista[i]) == str:
            if lista[i].isnumeric():
                if len(lista[i]) == 1:
                    lista[i] = '0' + lista[i]

    auxiliar = lista[:]
    lista.sort()

    return auxiliar == lista


def main():

    n = int(input())
    lista = []
    for a in range(n):
        inserir = input().strip()
        lista.append(inserir)

    if esta_ordenado(lista):
        print("lista ordenada".upper())
    else:
        print("lista não ordenada".upper())

    pass


if __name__ == "__main__":
    main()
