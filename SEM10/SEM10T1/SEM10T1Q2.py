"""Programa que mostra quantos dos números digitados pelo usuário são pares ou ímpares"""


def e_par(n: int = int):
    return 'par' if n % 2 == 0 else 'ímpar'


def quantos_pares_e_quantos_impares():
    numero_de_inserts = 100
    passo_a_passo = 1
    soma_mais_um_par = 0
    soma_mais_um_impar = 0

    for i in range(1, numero_de_inserts, passo_a_passo):
        entrada = int(input())

        if 'par' == e_par(entrada):
            soma_mais_um_par += 1
        elif 'ímpar' == e_par(entrada):
            soma_mais_um_impar += 1

    par = soma_mais_um_par
    impar = soma_mais_um_impar
    return par, impar


quantidade_de_pares, quantidade_de_impares = quantos_pares_e_quantos_impares()
qp, qi = quantidade_de_pares, quantidade_de_impares


print(f'Foram inseridos {qp} números pares e {qi} números ímpares.')
