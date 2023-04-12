# Questão 05
# O programa calcula a media de três notas


def resultado_alunos(n1, n2='0', n3='0'):
    
    n1, n2, n3 = int(n1), int(n2), int(n3)

    notas = n1 + n2 + n3
    media = notas / 3
    
    if n3 > 8 and media < 10:
        media += 1

        if media >= 10:
            media = 10
            return media
        return media
        
    return media


def main():
    print('Digite três notas para calcular uma média')
    a = input('Primeira nota: ').strip()
    b = input('Segunda nota: ').strip()
    c = input('Terceira nota: ').strip()

    print(f'A media final foi {resultado_alunos(a, b, c):.2f}')



if __name__=='__main__':
    main()
