# Programa que mostra quantos dos números digitados pelo usuário são pares ou ímpares
def e_par(n: int | float):
    return 'par' if n % 2 == 0 else 'ímpar'


def main():
    impares = pares = 0
    ##
    for i in range(100):
        # Entrada de dados
        entrada = int(input())
        if 'par' == e_par(entrada):
            pares += 1
        elif 'ímpar' == e_par(entrada):
            impares += 1

    print(f'Foram inseridos {pares} números pares')
    print(f'e {impares} números ímpares.')


if __name__ == "__main__":
    main()
