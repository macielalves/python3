def comprimento(item):
    count = 0
    for _ in item:
        count += 1

    return count


def maximo(item):
    a = 0
    maior = item[a]
    for i, num in enumerate(item):
        if num > maior:
            maior = num
            a = i

    return a, maior


def media(lista):
    if lista:
        s = 0
        for i in lista:
            s += i
        return round(s / comprimento(lista), 2)


def indice_maior_que_media(lista, media):
    c = []
    for i, num in enumerate(lista):
        if num > media:
            c.append(i)

    return c


def main():
    nomes = []
    alturas = []
    for _ in range(12):
        nome = input("Digite o nome do jogador: ").strip()
        altura = float(input("Digite a altura do jogador: "))
        nomes.append(nome), alturas.append(altura)

    indice_do_maior, maior = maximo(alturas)
    media_de_alturas = media(alturas)
    indices = indice_maior_que_media(alturas, media_de_alturas)

    print(f'JOGADOR MAIS ALTO DO TIME\n{nomes[indice_do_maior]}\n{maior:.2f}')
    print(f'ALTURA MÉDIA DO TIME\n{media_de_alturas:.2f}')
    print('JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')
    for i in indices:
        print(nomes[i])
        print(f'{alturas[i]:.2f}')
    pass


if __name__ == "__main__":
    main()
