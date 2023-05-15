def meses_para_comprar_carro(poupanca, rendimento_poupanca, preco_carro, taxa_aumento_carro):
    meses = 0

    while poupanca < preco_carro:
        poupanca += poupanca * rendimento_poupanca / 100
        preco_carro += preco_carro * taxa_aumento_carro / 100
        meses += 1

    return meses


def main():
    poupanca = 10000
    rendimento_poupanca = 0.7
    preco_carro = float(input("Digite o preço do carro hoje: "))
    taxa_aumento_carro = 0.4

    meses_necessarios = meses_para_comprar_carro(poupanca, rendimento_poupanca, preco_carro, taxa_aumento_carro)

    print(f"Serão necessários {meses_necessarios} meses para comprar o carro à vista.")


if __name__ == "__main__":
    main()
