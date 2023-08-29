def _conceito(n: float):
    if n >= 8.5:
        return 'A'
    elif n >= 7.:
        return 'B'
    elif n >= 5.:
        return 'C'
    elif n >= 4.:
        return 'D'
    elif n >= 0.:
        return 'E'


def main():
    while True:
        try:
            nota = float(input())
        except ValueError:
            print('Valor inválido.')
        else:
            if 0 <= nota <= 10:
                conceito = _conceito(nota)
                print(conceito)
                break
            else:
                print('Nota inválida.')


if __name__ == '__main__':
    main()
