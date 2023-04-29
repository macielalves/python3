valor = float(input())
n = 1
for i in range(24):
    valor_parcelado = valor / n
    print(f'{n}x de R$ {valor_parcelado:.2f}')
    n += 1
