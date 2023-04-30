# Escreva um programa que leia um conjunto de 100 e mostre a média dos mesmos!
import random
n = 100
soma = 0
# n é a quantidade de vezes que executará o loop
for i in range(n):
    soma += int(input())

media = soma / n

print('%.2f' % media)
