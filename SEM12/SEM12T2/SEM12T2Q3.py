def valor_de_H(n):
    h = 0.0

    for a in range(1, n + 1):
        h += 1 / a

    return h


def main():
    n = int(input("Digite um número inteiro: "))

    valor_H = valor_de_H(n)

    print(f"O valor de H para n = {n} é {valor_H}.")


if __name__ == "__main__":
    main()
