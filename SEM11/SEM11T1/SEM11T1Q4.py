def main():
    numeros = input().strip()

    if numeros.isnumeric():
        print(numeros[::-1])

    # invertidos = 0
    # resultado = ''
    # while True:
    #     invertidos = (numero % 10)
    #     numero //= 10
    #     resultado += str(invertidos)
    #
    #     if numero <= 0 and invertidos != 0:
    #         print(f'{resultado}')
    #         break
    # numero = int(input('Digite um número: '))


if __name__ == "__main__":
    main()

