def lista_invertida(tamanho_da_lista):
    lista = []
    for i in range(tamanho_da_lista):
        real = float(input(f"Digite um número real: "))
        real = round(real, 4)
        lista.insert(0, real)

    return lista


def calcula_notas(n):
    notas = []
    for i in range(n):
        nota = round(float(input("Digite uma nota: ")), 1)
        notas.append(nota)

    return notas


def media_lista(lista):
    tamanho = len(lista)
    soma = 0
    for n in range(tamanho):
        soma += lista[n]
    try:
        media = round(soma / tamanho, 1)
    except ZeroDivisionError:
        media = 0

    return media if lista else "SEM NOTAS"


def letras_lidas(n):
    vogais = []
    maiusculas = []
    if n != 0:
        for i in range(n):
            abc = input("Digite uma letra: ")[0]
            if abc.lower() in ('a', 'e', 'i', 'o', 'u'):
                vogais.append(abc)
            elif abc.isalpha():
                maiusculas.append(abc)

    return vogais, maiusculas


def main():
    n = int(input("Digite a quantidade de itens de sua lista: "))
    print(lista_invertida(n))
    notas = calcula_notas(n)
    media = media_lista(notas)
    print(notas)
    print(f" A media das notas é {media}")
    vogais, maiusculas = letras_lidas(n)
    print(f'Vogais digitadas: {len(vogais)}')
    print("Consoantes:", maiusculas)


if __name__ == "__main__":
    main()
