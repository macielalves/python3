def enumera(lista):
    a, count, aux = -len(lista), 0, []
    while a < 0:
        aux.append((count, lista[a]))
        count += 1
        a += 1
    return aux


def main():
    a = []
    for _ in range(10):
        a.append(int(input(f"Digite um numero {_+1} de 10: ")))

    p = 0
    maior = a[p]
    for i, n in enumera(a):
        if n > maior:
            maior, p = n, i

    print(f'{a}\n{maior}\n{p}')
    pass


if __name__ == "__main__":
    main()
