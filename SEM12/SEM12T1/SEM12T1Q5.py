# def simular_populacao_dodos(populacao_inicial):
#     populacao = populacao_inicial
#     populacao_original = populacao_inicial
#
#     print("Ano, Nascimentos, Mortes, População")
#
#     for ano in range(1600, 10000):
#         nascimentos = int(populacao * 0.01)
#         mortes = int(populacao * 0.06)
#         populacao -= mortes
#         populacao += nascimentos
#
#         print(f"{ano}, {nascimentos}, {mortes}, {populacao}")
#
#         if populacao < populacao_original * 0.1:
#             break
#
# populacao_inicial = int(input("Digite a população inicial de dodôs em 1600: "))
#
# simular_populacao_dodos(populacao_inicial)


def simular_populacao_dodos(populacao_inicial, ano_final):
        populacao = populacao_inicial

        for ano in range(1600, ano_final + 1):
            animais_mortos = populacao * 0.06
            animais_sobreviventes = (populacao - animais_mortos) * 0.01
            populacao = animais_sobreviventes

        return int(populacao)


def main():
    populacao_inicial = int(input("Digite a população inicial de dodôs: "))
    ano_final = int(input("Digite o ano final da simulação: "))

    populacao_final = simular_populacao_dodos(populacao_inicial, ano_final)

    print(f"A população de dodôs no ano {ano_final} seria de aproximadamente {populacao_final} indivíduos.")


if __name__ == "__main__":
    main()
