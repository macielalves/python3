"""Programa que mostra quantos dos números digitados pelo usuário são pares ou ímpares"""


def e_par(n: int = int):
    return 'par' if n % 2 == 0 else 'ímpar'


def quantos_pares_e_quantos_impares():
    numero_de_inserts = 100
    passo_a_passo = 1
    par = 0
    impar = 0

    for i in range(0, numero_de_inserts, passo_a_passo):
        entrada = int(input())

        if 'par' == e_par(entrada):
            par += 1
        elif 'ímpar' == e_par(entrada):
            impar += 1

    return par, impar


quantidade_de_pares, quantidade_de_impares = quantos_pares_e_quantos_impares()
qp, qi = quantidade_de_pares, quantidade_de_impares


print(f'Foram inseridos {qp} números pares')
print(f'e {qi} números ímpares.')
