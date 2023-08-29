def verifica_data_se_e_valida(dia, mes, ano):
    ano_valido = True if 0 < ano <= 9999 else False
    # and (ano % 100 != 0 or ano % 400 == 0)
    bissexto = 1 if ano % 4 == 0 else 0

    mes_valido = True if 0 < mes <= 12 else False

    meses = [31, (28 + bissexto), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dia_do_mes = 30
    if mes_valido:
        dia_do_mes = meses[mes - 1]

    dia_e_valido = True if 0 < dia <= dia_do_mes else False

    return True if dia_e_valido and mes_valido and ano_valido else False


def date_clean(data='0'):
    # testa se o valor não é string
    if data != str:
        # um limpador de sinais simples e espaços em branco
        data = str(data).strip().replace(' ', '').replace('/', '')

    return data


def separa_data(data):
    a = data[4:]
    m = data[2:4]
    d = data[:2]

    return int(d), int(m), int(a)


def main():

    # Entrada de dados
    data_in = input('Digite uma data no tipo DDMMAAAA: ')

    # Processamento
    data = date_clean(data_in)
    dia, mes, ano = separa_data(data)
    data_valida = verifica_data_se_e_valida(dia, mes, ano)

    # Saída
    print(data_valida)


if __name__ == '__main__':
    main()
