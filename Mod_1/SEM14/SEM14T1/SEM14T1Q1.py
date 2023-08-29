def comprimento(item):
    count = 0
    for _ in item:
        count += 1

    return count


def inverter(item):
    # invertendo na ordem de índice
    return item[::-1]


def minimo(item):
    # recebe o primeiro item da lista como comparador
    menor = item[0]
    for i in item:
        menor = i if i < menor else menor

    return menor


def maximo(item):
    a = 0
    maior = item[a]
    for i, num in enumerate(item):
        if num > maior:
            maior = num
            a = i

    return a, maior


def soma(item):
    s = 0
    for i in item:
        s += i

    return s


def main():
    lista = []
    while 'Entrada':
        item = int(input("Digite 0 para sair ou qualquer outro número para continuar adicionando: "))
        if item == 0:
            break
        lista.append(item)

    _, maior = maximo(lista)
    print("Lista de números digitados:", lista)
    print("Tamanho da lista:", comprimento(lista))
    print("Lista na ordem inversa:", inverter(lista))
    print("Menor número", minimo(lista))
    print("Maior número", maior)
    print("Soma dos numeros da lista:", soma(lista))
    pass


if __name__ == "__main__":
    main()
