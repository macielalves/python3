def verificar_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):  # numero ** 0.5 == raiz_quadrada(numero)
        if numero % i == 0:
            return False

    return True


def main():
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))

    print(f"Números primos entre {x} e {y}:")
    for numero in range(x, y + 1):
        if verificar_primo(numero):
            print(numero)


if __name__ == "__main__":
    main()
