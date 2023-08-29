def main():
    populacao_inicial = int(input("Digite a população inicial de dodôs no início de 1600: "))

    ano = 1600
    populacao_atual = populacao_inicial

    while populacao_atual >= populacao_inicial * 0.1:
        nascimentos = populacao_atual * 0.01
        mortes = populacao_atual * 0.06
        populacao_atual += nascimentos - mortes

        print(f"{ano:.0f},{nascimentos:.0f},{mortes:.0f},{populacao_atual:.0f}")

        ano += 1


if __name__ == "__main__":
    main()
