# Questão 05
# Ordena três numeros inteiros de forma crecente


def ord_crescente(n1, n2=0, n3=0):
    if n1 >= n2 >= n3:
        return f'{n3}\n{n2}\n{n1}'

    elif n1 >= n3 >= n2:
        return f'{n2}\n{n3}\n{n1}'

    elif n2 >= n1 >= n3:
        return f'{n3}\n{n1}\n{n2}'

    elif n2 >= n3 >= n1:
        return f'{n1}\n{n3}\n{n2}'

    elif n3 >= n1 >= n2:
        return f'{n2}\n{n1}\n{n3}'

    elif n3 >= n2 >= n1:
        return f'{n1}\n{n2}\n{n3}'


def main():
    a = int(input('Digite um número inteiro: '))
    b = int(input('Digite outro número inteiro: '))
    c = int(input('Digite um terceiro número inteiro: '))
    print(ord_crescente(a, b, c))


if __name__ == '__main__':
    main()
