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
    pop = int(input('Digite um valor para população: '))

    cidades = carrega_cidades()
    print(f'CIDADES COM MAIS DE {pop} HABITANTE{"S" if pop != 1 else ""}:'.upper())
    for d_city in cidades:
        if d_city[5] >= pop:
            print('IBGE:',d_city[1], '-', d_city[2]+'('+d_city[0]+')', '- POPULAÇÃO:', d_city[5])
    ...


if __name__ == "__main__":
    main()
