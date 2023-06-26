# 1º armazenar a temperatura média de cada mês do ano
# 2º calcular a média de temperatura anual
# 3º mostrar em Kelvin todas as temperaturas acima da média anual e em que mês elas ocorreram
# (mostrar o mês por extenso: 1 - Janeiro, 2 - Fevereiro,...)

def soma_temperaturas(temperaturas: list):
    soma = 0
    for temp in temperaturas:
        soma += temp
        soma = round(soma, 2)  # malandragem
    return soma


def main():
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

    temperaturas = []

    for i in range(12):
        temperatura = float(input(f"Digite a temperatura média do mês de {meses[i]}: "))
        escala = input().strip()

        if escala == "C":
            temperatura = temperatura + 273.15
        elif escala == "F":
            temperatura = (temperatura - 32) * 5 / 9 + 273.15

        temperaturas.append(temperatura)

    media_anual = soma_temperaturas(temperaturas) / len(temperaturas)

    print("TEMPERATURA MÉDIA ANUAL")
    print(f"{round(media_anual, 2)}K")

    print("TEMPERATURAS ACIMA DA MÉDIA ANUAL:")
    for i in range(len(temperaturas)):
        if temperaturas[i] > media_anual:
            print(f"{meses[i]}: {round(temperaturas[i], 2)}K")


if __name__ == "__main__":
    main()
