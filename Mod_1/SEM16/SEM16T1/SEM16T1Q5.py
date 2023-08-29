def preenchimento_de_faturas(dim_0, dim_1, dim_2):
    dim_i = []
    for i in range(dim_0):
        dim_j = []
        for j in range(dim_1):
            dim_k = []
            for k in range(dim_2):
                dim_k.append(float(input("Entre com o valor de fatura do mês")))
            dim_j.append(dim_k)
        dim_i.append(dim_j)
    return dim_i


def soma(lista):  # filial, lista de valores em uma filial
    s = 0
    for i in lista:
        s += i
    return round(s)


def main():
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    ano = 2014

    faturamento_anual = preenchimento_de_faturas(4, 3, 12)  # anos, filiais, meses
    soma_total = 0

    for _ in faturamento_anual:
        soma_filial = 0
        for i, j in enumerate(_):
            for u, v in enumerate(j):  # j referente a lista da filial
                print(f"{ano};Filial {i+1};{meses[u]};{v:.0f}")

            aux = soma(j)
            soma_filial += aux
            print(f"Total {ano} Filial {i+1};{aux}".upper())
        soma_total += soma_filial
        print(f"Total {ano} Todas Filiais;{soma_filial}".upper())
        ano += 1
    print(f"Total Período Todas Filiais;{soma_total}".upper())


if __name__ == "__main__":
    main()
