def soma_lista(lista):
    soma = 0
    for indices in range(len(lista)):
        soma += lista[indices]

    return soma


def multiplica_lista(lista):
    mult = 1
    for indices in range(len(lista)):
        mult *= lista[indices]

    return mult


def main():
    # entrada de 10 números em uma lista
    numeros = []
    for i in range(10):
        numeros.append(int(input()))

    # processar soma e multiplicação
    soma = soma_lista(numeros)
    multiplicacao = multiplica_lista(numeros)

    # saída dos números digitados, sua soma e múltiplicação
    print(numeros)
    print(soma)
    print(multiplicacao)


if __name__ == "__main__":
    main()
