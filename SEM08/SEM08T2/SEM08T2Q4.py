def peso_ideal(al, g):
    if g == 1:
        return (72.7 * al) - 58
    elif g == 2:
        return (62.1 * al) - 44.7


def main():
    altura = float(input('Digite sua altura em metros(m): '))
    sexo = int(input('Você é \n[1]Homem \n[2]mulher \nDigite uma das opções acima: '))
    # 1 para homens
    # 2 para mulheres
    print('O peso ideal para você é {:.2f}'.format(peso_ideal(altura, sexo)))


if __name__=="__main__":
    main()