def dia_da_semana(n):
    if n == 1:
        return 'domingo'
    elif n == 2:
        return 'segunda-feira'
    elif n == 3:
        return 'terça-feira'
    elif n == 4:
        return 'quarta-feira'
    elif n == 5:
        return 'quinta-feira'
    elif n == 6:
        return 'sexta-feira'
    elif n == 7:
        return 'sábado'
    else:
        return 'valor inválido'


def main():
    n = int(input('Digite um número de 1 a 7: '))
    print(dia_da_semana(n))


if __name__ == '__main__':
    main()
