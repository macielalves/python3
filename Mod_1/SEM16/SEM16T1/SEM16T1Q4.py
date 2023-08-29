fabricantes = ('Fiat', 'Ford', 'GM', 'Wolkswagen')
anos = (2013, 2014, 2015, 2016, 2017, 2018)
Q_ANOS = 6


def maior_vendedor_do_ano(tabela, ano):
    coluna = None
    maior = None
    fab = None
    for a in range(Q_ANOS):
        if ano == anos[a]:
            coluna = a
    aux = 0
    for i in tabela:
        if maior is None:
            maior = i[coluna]
        if maior < i[coluna]:
            maior = i[coluna]
            fab = aux
        aux += 1

    return fab, maior


def ano_de_maior_volume(t):
    ano = None
    maior = None
    for i in range(Q_ANOS):
        soma = 0
        for lin in t:
            soma += lin[i]
        if maior is None:
            maior = soma
            ano = i
        elif maior < soma:
            maior = soma
            ano = i
    return ano, maior


def media_de_vendas_de_cada_fabricante(tab):
    medias = []
    for w in tab:
        soma = 0
        for v in w:
            soma += v
        medias.append(round(soma/len(w), 2))
    return medias


def main():
    tabela = []
    for i in range(4):
        linha = []
        for j in range(Q_ANOS):
            vendas = int(input(f"Fabricante {fabricantes[i]}| Digite a quantidade de vendas do ano {anos[j]}: "))
            linha.append(vendas)
        tabela.append(linha)

    print(anos)
    ano = int(input("Digite um ano: "))
    indice, n_unidades = maior_vendedor_do_ano(tabela, ano)
    ano_de_pico, u_vol_geral = ano_de_maior_volume(tabela)
    media_fiat, media_ford, media_gm, media_wkgen = media_de_vendas_de_cada_fabricante(tabela)

    print(f"A fabricante que mais vendeu em {ano} foi a {fabricantes[indice]} com {n_unidades} mil unidades.")
    print(f"O ano de maior volume geral de vendas foi {anos[ano_de_pico]} com {u_vol_geral} mil unidades.")
    print("A média anual de vendas de cada fabricante entre 2013 e 2018 foi:")
    print(f"A {fabricantes[0]} vendeu em média {media_fiat} unidades por ano.")
    print(f"A {fabricantes[1]} vendeu em média {media_ford} unidades por ano.")
    print(f"A {fabricantes[2]} vendeu em média {media_gm} unidades por ano.")
    print(f"A {fabricantes[3]} vendeu em média {media_wkgen} unidades por ano.")


if __name__ == '__main__':
    main()
