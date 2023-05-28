def notas_maiores_que_seis(lista):
    maiores_que_seis = []
    for i in range(len(lista)):
        if lista[i] >= 6.:
            maiores_que_seis.append(i)

    return maiores_que_seis


def main():
    # Entrada de notas
    notas = []
    for n in range(50):
        notas.append(round(float(input('Digite uma nota: ')), 2))  # round(float(input()), 2)

    # Processamento de notas maiores que seis
    indice_de_notas = notas_maiores_que_seis(notas)

    # Saída das maiores notas
    print('Os indices das maiores notas são:', indice_de_notas)
    pass


if __name__ == "__main__":
    main()
