# def ler_conjunto_de_cem():
x = 0
raio = 4
for n in range(raio):
    n += 1
    numero = int(input())
    if numero > x:
        x = numero

print(x)
