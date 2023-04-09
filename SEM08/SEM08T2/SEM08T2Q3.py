def edivisivel(n):
    if n >= 0:
        if n % 3 == 0 or n % 5 == 0:
            t1=t2=t3=''
            if n % 3 == 0 :
                t1 = 'FIZZ'
            if n % 5 == 0:
                t2 = 'BUZZ'
            if n % 3 == 0 and n % 5 == 0:
                t3 = t1 + t2
                t1 = t2 = ''

            return t1 + t2 + t3
        else:
            return n


def main():
    print('Mostra FIZZ se for divisível por 3, BUZZ se divisível por 5, se divisível por 3 e por 5 mostra FIZZBUZZ e se não for divisível mostra o próprio número!')
    n = int(input('Digite um número: '))
    print(edivisivel(n))


if __name__=="__main__":
    main()