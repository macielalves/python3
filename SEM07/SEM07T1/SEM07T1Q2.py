# Questão 02
# O programa recebe um numero e retorna True se o numero for ímpar e False caso contrario

# isodd 'é ímpar' em inglês
def isodd(n):
    return not n % 2 == 0


def main():
    num = int(input('Digite um número: '))
    print('%s' % (isodd(num)))


if __name__=='__main__':
    main()
