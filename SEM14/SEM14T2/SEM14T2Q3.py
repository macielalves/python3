def remove_clone(lista: list):
    a = []
    for b in lista:
        if b not in a:
            a.append(b)
    return a


def main():
    lista = []
    for _ in range(20):
        lista.append(int(input("Insira numeros para sua lista: ")))

    lista_sem_repetidos = remove_clone(lista)
    print("Lista sem repetição de algarismos", lista_sem_repetidos)
    pass


if __name__ == "__main__":
    main()
