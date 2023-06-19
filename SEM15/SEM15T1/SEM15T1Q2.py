# função de conversão de temperatura para celsius
def celsius(t):
    if t[1] == 'F':
        return (t[0] - 32) * (5/9)
    elif t[1] == 'K':
        return t[0] - 273

    return t[0]


# função de conversão de temperatura para fahrenheit
def fahrenheit(t):
    if t[1] == 'C':
        return t[0] * (9/5) + 32
    elif t[1] == 'K':
        return (t[0] - 273) * 1.8 + 32

    return t[0]


# função de conversão de temperatura para kelvin
def kelvin(t):
    if t[1] == 'C':
        return t[0] + 273
    elif t[1] == 'F':
        return (t[0] - 32) * (5/9) + 273

    return t[0]


def converte_temperatura(valor, base):
    # valor é uma tupla (a, 'b') e base é uma string
    if base == 'C':
        return celsius(valor)
    elif base == 'F':
        return fahrenheit(valor)
    elif base == 'K':
        return kelvin(valor)


def soma_temperaturas(temperaturas):
    # temperaturas é uma lista que contem as tuplas
    soma = 0
    # E é o segundo item da segunda tupla. Base do cálculo térmico.
    E = temperaturas[1][1]
    for i in temperaturas:
        soma += converte_temperatura(i, E)

    return round(soma, 4), E


def main():
    temperaturas = []
    for _ in range(2):
        t = round(float(input('Digite um valor de temperatura: ')), 4)
        e = input('Digite a escala da temperatura digitada: ').upper()[0]
        temperaturas.append((t, e))

    print(soma_temperaturas(temperaturas))


if __name__ == "__main__":
    main()