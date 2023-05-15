def calcular_tempo_crescimento(populacao_a, taxa_a, populacao_b, taxa_b):
    tempo = 0

    while populacao_a >= populacao_b:
        populacao_a *= (1 + taxa_a / 100)
        populacao_b *= (1 + taxa_b / 100)
        tempo += 1

    return tempo


def main():
    populacao_a = int(input("Informe a população do país A: "))
    taxa_a = 2

    populacao_b = int(input("Informe a população do país B: "))
    taxa_b = 3

    tempo_necessario = calcular_tempo_crescimento(populacao_a, taxa_a, populacao_b, taxa_b)

    print(f"Serão necessários {tempo_necessario} anos para a população do país B ultrapassar a população do país A.")


if __name__ == "__main__":
    main()
