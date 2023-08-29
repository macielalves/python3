def maior_que_13(idades):
    maiores_que_13 = []
    for i, idade in enumerate(idades):
        if idade > 13:
            maiores_que_13.append(i)
    return maiores_que_13


def media_de_alturas(alturas):
    length = len(alturas)
    s = 0
    for i in alturas:
        s += i

    return round(s / length, 2)


def altura_abaixo_da_media(maiores_que_13, media):
    a = []
    for i, altura in enumerate(maiores_que_13):
        if altura < media:
            a.append(i)

    return a


def main():
    nomes = []
    idades = []
    alturas = []
    resultado = []
    for i in range(30):
        nomes.append(input(f'Digite o nome do aluno {i+1} de 30: ').strip())
        idades.append(int(input(f'Digite a idade do aluno: ')))
        alturas.append(round(float(input(f'Digite a altura do aluno: ')), 2))

    a = maior_que_13(idades)
    media_das_alturas_dos_alunos = media_de_alturas(alturas)
    # a variável "a" é o índice de alturas dentre os alunos com idade maior que 13
    b = altura_abaixo_da_media(alturas, media_das_alturas_dos_alunos)
    for i in a:
        for j in b:
            if i == j:
                resultado.append(j)

    print('MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')
    for k in resultado:
        print(nomes[k])
    pass


if __name__ == "__main__":
    main()
