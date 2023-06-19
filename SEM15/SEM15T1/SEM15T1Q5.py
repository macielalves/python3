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

    mes = int(input('Digite um valor para o mês: '))
    pop = int(input('Digite um valor de população: '))

    cidades = carrega_cidades()

    print(f"cidades com mais de {pop} habitantes e aniversário em {meses[mes - 1]}:".upper())
    for dados in cidades:
        if dados[5] >= pop and dados[4] == mes:
            print(f'{dados[2]}({dados[0]}) tem {dados[5]} habitantes e faz aniversário em {dados[3]} de {meses[mes - 1]}.')
    ...


if __name__ == "__main__":
    main()
