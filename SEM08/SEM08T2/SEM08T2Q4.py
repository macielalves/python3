def peso_ideal(al, g):
    if g == 1:
        return (72.7 * al) - 58
    elif g == 2:
        return (62.1 * al) - 44.7


altura = float(input())
sexo = int(input())
# 1 para homens
# 2 para mulheres
print('{:.2f}'.format(peso_ideal(altura, sexo)))