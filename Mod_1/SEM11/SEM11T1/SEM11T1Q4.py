def main():
    numero = int(input())
    inverso = 0
    while numero > 0:
        unidades = numero % 10
        inverso = (inverso*10) + unidades
        numero //= 10

    print(inverso)


if __name__ == "__main__":
    main()

