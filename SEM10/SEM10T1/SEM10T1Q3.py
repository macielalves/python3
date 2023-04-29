"""Escreva um programa que leia um conjunto de 100 e mostre a média dos mesmos!"""
n = 100
"""n é a quantidade estática para obter uma média de 100 números"""
for i in range(n):
    numero = int(input())
    soma = numero + 1

media = soma / n


print('%.2f' % media)
