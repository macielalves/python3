def main():
    maior = menor = None
    pessoas = 0
    soma = 0
    while True:
        try:
            idade = int(input())
        except ValueError:
            print('Insira uma valor válido!')
            continue
        else:
            if idade == 0:
                break
            else:
                soma += idade
                pessoas += 1

            maior = idade if 0 < idade >= (maior if maior is not None else idade) else maior
            menor = idade if 0 < idade <= (menor if menor is not None else idade) else menor

    #
    if pessoas != 0:
        media = soma / pessoas
        print(pessoas)
        print(f'{media:.2f}')
        print(menor)
        print(maior)


if __name__ == "__main__":
    main()
