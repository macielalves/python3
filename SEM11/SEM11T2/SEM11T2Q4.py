def main():
    soma = 0
    while True:
        print(
            "CÓDIGO  PRODUTO         PREÇO (R$)",
            "H       Hamburger       5,50",
            "C       Cheeseburger    6,80",
            "M       Misto Quente    4,50",
            "A       Americano       7,00",
            "Q       Queijo Prato    4,00",
            "X       PARA TOTAL DA CONTA",
            sep='\n'
        )

        codigo = input().strip().upper()[0]

        if codigo == 'H':
            soma += 5.5
        elif codigo == 'C':
            soma += 6.8
        elif codigo == 'M':
            soma += 4.5
        elif codigo == 'A':
            soma += 7.
        elif codigo == 'Q':
            soma += 4.
        elif codigo == 'X':
            break
        else:
            print('Opção inválida.')

    print(f'{soma:.2f}')


if __name__ == "__main__":
    main()
