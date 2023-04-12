#inicio da main
def main():
    a = input().strip()
    b = input().strip()
    c = input().strip()
    print(f'{resultado_alunos(a, b, c):.2f}')




#final da main
def resultado_alunos(n1, n2=0, n3=0):
    #não converte complexo; não converte não numeros,  (abcde...); Converte do tipo exp => 10e10;
    n1, n2, n3 = float(n1), float(n2), float(n3)

    notas = n1 + n2 + n3
    media = notas / 3
    
    if n3 > 8 and media < 10:
        media += 1;
        return media

    return media


if __name__=='__main__':
    main()
