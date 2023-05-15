def calcular_numero_da_sorte(data_nascimento):
        soma_digitos = 0
        for i in range(8):
            soma_digitos += data_nascimento % 10
            data_nascimento //= 10

        return soma_digitos


def main():
    data_nascimento = int(input("Digite a data de nascimento no formato ddmmaaaa: "))
    numero_da_sorte = calcular_numero_da_sorte(data_nascimento)

    print(f"O número da sorte é {numero_da_sorte}.")


if __name__ == "__main__":
    main()
