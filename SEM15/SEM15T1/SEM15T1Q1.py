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


# função que retorna qual a maior temperatura e sua escala em uma lista
def maior_temperatura(temperaturas):
    maior = temperaturas[0][0]
    E = temperaturas[0][1]
    flag_maior = 0
    for indices, t in enumerate(temperaturas):
        aux = converte_temperatura(t, E)
        if aux > maior:
            flag_maior = indices
            maior = t[0]
    return temperaturas[flag_maior]


def main():
    temperaturas = []
    for _ in range(2):
        t = round(float(input('Digite o valor da temperatura: ')), 4)
        e = input('Escala: ').upper()[0]
        temperaturas.append((t, e))

    print(maior_temperatura(temperaturas))


if __name__ == "__main__":
    main()