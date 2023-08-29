# Recebe um valor e o parcela de 1 a 24 vezes
valor = float(input())
for i in range(24):
    valor_parcelado = valor / (i+1)
    print(f'{i+1}x de R$ {valor_parcelado:.2f}')
