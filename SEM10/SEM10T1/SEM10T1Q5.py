# O programa que mostra qual o maior valor digitado em um conjunto de 100 números
x = 0
for i in range(100):
    numero = int(input())
    if x <= numero:
        x = numero

print(x)
