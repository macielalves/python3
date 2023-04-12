# Questão 04
# recebe a data de nacimento do usuário retorna o signo


def signo(dd, mm):
    if 21 <= dd <= 31 and mm == 3 or 1 <= dd <= 19 and mm == 4:
        return 'Áries'

    elif 20 <= dd <= 31 and mm == 4 or 1 <= dd <= 20 and mm == 5:
        return 'Touro'

    elif 21 <= dd <= 31 and mm == 5 or 1 <= dd <= 21 and mm == 6:
        return 'Gêmeos'

    elif 22 <= dd <= 31 and mm == 6 or 1 <= dd <= 22 and mm == 7:
        return 'Câncer'

    elif 23 <= dd <= 31 and mm == 7 or 1 <= dd <= 22 and mm == 8:
        return 'Leão'

    elif 23 <= dd <= 31 and mm == 8 or 1 <= dd <= 22 and mm == 9:
        return 'Virgem'

    elif 23 <= dd <= 31 and mm == 9 or 1 <= dd <= 22 and mm == 10:
        return 'Libra'

    elif 23 <= dd <= 31 and mm == 10 or 1 <= dd <= 21 and mm == 11:
        return 'Escorpião'

    elif 22 <= dd <= 31 and mm == 11 or 1 <= dd <= 21 and mm == 12:
        return 'Sagitário'

    elif 22 <= dd <= 31 and mm == 12 or 1 <= dd <= 19 and mm == 1:
        return 'Capricórnio'

    elif 20 <= dd <= 31 and mm == 1 or 1 <= dd <= 18 and mm == 2:
        return 'Aquário'

    elif 19 <= dd <= 31 and mm == 2 or 1 <= dd <= 20 and mm == 3:
        return 'Peixes'


def main():

    dia = int(input('Digite o dia de seu nascimento: ').strip())
    mes = int(input('Digite o mês de seu nacimento: ').strip())
    print('Seu signo é %s' % signo(dia, mes))

if __name__ == '__main__':
    main()
