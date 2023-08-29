def soma5ou8(n=0):
    if n % 2 == 0:
        n += 5
    elif n % 2 == 1:
        n += 8
    return n


def main():
    print('Soma por 5 se for par e soma por 8 se for impar')
    n = int(input('Digite um número: '))
    print(f'O resultado é {soma5ou8(n)}')


if __name__=="__main__":
    main()