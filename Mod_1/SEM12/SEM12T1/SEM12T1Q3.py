def tempo_crescimento(populacao_a, taxa_a, populacao_b, taxa_b):
    tempo = 0
    maior_populacao = max(populacao_a, populacao_b)
    menor_populacao = min(populacao_a, populacao_b)

    while maior_populacao >= menor_populacao:
        maior_populacao *= (1 + taxa_a / 100)
        menor_populacao *= (1 + taxa_b / 100)
        tempo += 1

    return tempo


def main():
    populacao_a = int(input("Digite a quantidade de pessoas do país A: "))
    taxa_a = 2

    populacao_b = int(input("Digite a quantidade de pessoas do país B: "))
    taxa_b = 3

    tempo_necessario = tempo_crescimento(populacao_a, taxa_a, populacao_b, taxa_b)

    print(f"Serão necessários {tempo_necessario} anos para a população do país B ultrapassar a população do país A.")


if __name__ == "__main__":
    main()
