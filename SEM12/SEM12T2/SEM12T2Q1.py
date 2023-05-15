def fatorial(numero):
    if numero == 0:
        return 1

    fat = 1
    for i in range(1, numero + 1):
        fat *= i

    return fat


def main():
    numero = int(input("Digite um número inteiro: "))

    resultado = fatorial(numero)

    print(f"O fatorial de {numero} é {resultado}")


if __name__ == "__main__":
    main()
