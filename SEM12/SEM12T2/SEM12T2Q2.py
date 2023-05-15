def fibonacci(n):
    fib = [0, 1]  # Inicializando os primeiros dois termos da sequência

    for i in range(2, n):
        termo_atual = fib[i - 1] + fib[i - 2]
        fib.append(termo_atual)

    return fib


def main():
    n = int(input("Digite um número maior ou igual a 2: "))

    termos_fibonacci = fibonacci(n)

    termos = ''
    for termo in termos_fibonacci:
        termos += str(termo) + ', '

    termos = termos.rstrip(", ")
    print(f"{termos}")


if __name__ == "__main__":
    main()
