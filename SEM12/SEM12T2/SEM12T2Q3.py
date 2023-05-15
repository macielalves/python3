def valor_de_H(n):
    h = 0.0

    for a in range(1, n + 1):
        h += 1 / a

    return h


def main():
    n = int(input("Digite um número para n fatores da série H = 1 + 1/2 + 1/3+ ... + 1/n : "))

    valor_H = valor_de_H(n)

    print(f"O valor de H é {valor_H:.4f}")


if __name__ == "__main__":
    main()
