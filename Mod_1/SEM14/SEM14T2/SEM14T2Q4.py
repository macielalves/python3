def produto_escalar(x, y):
    xy = 0
    frufru = ''
    for i in range(len(x)):
        xy = x[i] * y[i] + xy
        frufru = frufru + f"({x[i]} x {y[i]}) {'+' if i != len(x)-1 else '='} "

    return frufru + str(xy)
    pass


def main():
    a, b = [], []
    for _ in range(5):
        a.append(int(input(f'Digite um numero para x. {_+1} de 5: ')))
    for _ in range(5):
        b.append(int(input(f'Digite um numero para y. {_+1} de 5: ')))

    print(a)
    print(b)
    print(produto_escalar(a, b))
    pass


if __name__ == "__main__":
    main()
