def media(nota1, nota2, nota3, nota4, nota5):
    return (nota1 + nota2 + nota3 + nota4 + nota5) / 5  


def mostra_maior(med, n1, n2, n3, n4, n5):
    if n1 > med:
        print(f'Primeira nota: {n1:.2f}')
    if n2 > med:
        print(f'Segunda nota: {n2:.2f}')
    if n3 > med:
        print(f'Terceira nota: {n3:.2f}')
    if n4 > med:
        print(f'Quarta nota: {n4:.2f}')
    if n5 > med:
        print(f'Quinta nota: {n5:.2f}')
    

def main():
    n1 = int(input('Primeira nota: '))
    n2 = int(input('Segunda nota: '))
    n3 = int(input('Terceira nota: '))
    n4 = int(input('Quarta nota: '))
    n5 = int(input('Quinta nota: '))
    
    md = media(n1, n2, n3, n4, n5)
    
    print(f'Sua média é {md:.2f}')
    print('Nota maior que a média:')
    mostra_maior(md, n1, n2, n3, n4, n5)


if __name__=='__main__':
    main()