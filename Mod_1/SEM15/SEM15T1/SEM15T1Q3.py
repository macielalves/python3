def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )

    arquivo.close()
    return resultado


def main():
    meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
             'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

    dia = int(input('Digite um valor para o dia: '))
    mes = int(input('Digite um valor para o mês: '))

    # o formato das saídas de tuplas são 6 itens para cada índice
    cidades = list(carrega_cidades())

    print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {meses[mes -1].upper()}:')
    while cidades:
        if (cidades[0][3] == dia) and (cidades[0][4] == mes):
            print(cidades[0][2]+f'({cidades[0][0]})')

        del cidades[0]
    ...


if __name__ == "__main__":
    main()
