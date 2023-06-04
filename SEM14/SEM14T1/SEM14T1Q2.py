# count reescrita usando só o básico
def count(item, p):
    c = 0
    for _ in item:
        c += 1 if p == _ else 0
    return c


def main():
    lista = []
    while "Rodando":
        n = int(input('Digite um numero. 0 para sair: '))
        if n == 0:
            break
        else:
            lista.append(n)

    p = int(input('Digite um numero para saber quantas vezes ele foi digitado: '))
    print(f'{lista}\n{p}\n{count(lista, p)}')
    pass


if __name__ == "__main__":
    main()
