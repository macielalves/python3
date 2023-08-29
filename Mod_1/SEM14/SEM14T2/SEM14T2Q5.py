def remove_clone(lista: list):
    a = []
    for b in lista:
        if b not in a:
            a.append(b)
    return a


def main():
    lista1, lista2, lista3 = [], [], []
    for _ in range(10):
        lista1.append(int(input("Digite um numero para o primeiro conjunto: ")))
    for _ in range(10):
        lista2.append(int(input("Digite um numero para o segundo conjunto: ")))

    lista3.extend(lista1)
    lista3.extend(lista2)
    lista4 = remove_clone(lista3)

    print(f'{lista4}')
    pass


if __name__ == '__main__':
    main()
