kg_morango = float(input('Digite a quantidade em quilograma de morango: '))
kg_maca = float(input('Digite a quantidade em quilograma de maçã: '))

preco_morango = preco_maca = total = 0.

preco_morango = kg_morango * 2.5 if kg_morango <= 5 else kg_morango * 2.2

preco_maca = kg_maca * 1.8 if kg_maca <= 5 else kg_maca * 1.5

total = preco_maca + preco_morango

if (kg_morango + kg_maca) > 8 or total > 25:
    total = total - total*1/10

print(f'O total a para é {total:.2f}')
