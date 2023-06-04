def lista_paralela(a, b):
    c = []
    for _, num in enumerate(a):
        c.append(num + b[_])

    return c


# OU
def soma_l(a, b):
    length_a, length_b = len(a), len(b)
    if length_b > length_a: a, b, length_a = b, a, length_b
    while length_a >= len(b): b.append(0)
    return [a[i] + b[i] for i in range(length_a)]


def main():
    a, b = [], []
    for i in range(20):
        a.append(int(input(f"{i+1}/20 Digite um numero para A: ")))

    for i in range(20):
        b.append(int(input(f"{+1}/20 Digite um numero para B: ")))

    print(f'{a}\n{b}\n{soma_l(a, b)}')
    pass


if __name__ == "__main__":
    main()
