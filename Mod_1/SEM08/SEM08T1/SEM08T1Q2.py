def data_mais_recente(d1, m1, a1, d2, m2, a2):
    if a1 > a2:
        return f'{d1}/{m1}/{a1}'
    elif a2 > a1:
        return f'{d2}/{m2}/{a2}'
    elif m1 > m2:
        return f'{d1}/{m1}/{a1}'
    elif m2 > m1:
        return f'{d2}/{m2}/{a2}'
    elif d1 > d2:
        return f'{d1}/{m1}/{a1}'
    elif d2 > d1:
        return f'{d2}/{m2}/{a2}'
    else:
        return f'{d1}/{m1}/{a1}' and f'{d2}/{m2}/{a2}'

def main():
    print('Comparador de datas, mostra a data mais recente')
    dia1 = int(input("Digite o dia da primeira data: "))
    mes1 = int(input("Digite o mês da primeira data: "))
    ano1 = int(input("Digite o ano da primeira data: "))

    dia2 = int(input("Digite o dia da segunda data: "))
    mes2 = int(input("Digite o mês da segunda data: "))
    ano2 = int(input("Digite o ano da segunda data: "))

    print(f'A data digitada mais recente é {data_mais_recente(dia1, mes1, ano1, dia2, mes2, ano2)}')

if __name__ == '__main__':
    main()