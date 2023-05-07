def main():
    salario = float(input())
    divida = float(input())
    # salario = 2000
    # divida = 100
    mes = 10
    ano = 2016
    periodo = 1

    while divida < salario:
        if mes == 12:
            mes = 0
            ano += 1
        mes += 1
        if mes == 3:
            salario += (salario * 5 / 100)

        divida += (divida * (15 / 100))
        periodo += 1

    print(mes)
    print(ano)


if __name__ == "__main__":
    main()
