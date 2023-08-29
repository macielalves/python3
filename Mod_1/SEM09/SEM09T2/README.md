># Semana 09

## Código de destaque:

```python
## código presente no arquivo SEM09T2Q4.py

# entrada de dados
kg_morango = float(input('Digite a quantidade em quilograma de morango: '))
kg_maca = float(input('Digite a quantidade em quilograma de maçã: '))

# zerando variáveis
preco_morango = preco_maca = total = 0.

# usando modelo de condição inline em filtragem de dados
preco_morango = kg_morango * 2.5 if kg_morango <= 5 else kg_morango * 2.2

# filtro de dados
preco_maca = kg_maca * 1.8 if kg_maca <= 5 else kg_maca * 1.5

# processando valor final
total = preco_maca + preco_morango

# ultima condicional com atribuição caso True
if (kg_morango + kg_maca) > 8 or total > 25:
    total = total - total*1/10

# saída de dados
print(f'O total a para é {total:.2f}')

```

## Mais um código bruto:

```python
def mostra_numero_por_extenso(n):
    if n < 1000:
        nome = ['', 'uma', 'duas', 'três', 'quatro', 'cinco', 'seis', 'sete',
                'oito', 'nove']
        c_n = ['', 'unidade', 'dezena', 'centena']  # casas numéricas

        c = n // 100
        d = n // 10 % 10
        u = n % 10

        ab_c = abs(c)  # valor absoluto
        ab_d = abs(d)
        ab_u = abs(u)

        centena_por_extenso = dezena_por_extenso = unidade_por_extenso = 0

        if -10 <= c < 10 and c != 0:
            centena_por_extenso = nome[ab_c] + ' ' + \
                c_n[3] + ('s' if ab_c > 1 else '')
        if -10 < d < 10 and d != 0:
            dezena_por_extenso = nome[ab_d] + ' ' + \
                c_n[2] + ('s' if ab_d > 1 else '')
        if -10 < u < 10 and u != 0:
            unidade_por_extenso = nome[ab_u] + ' ' + \
                c_n[1] + ('s' if ab_u > 1 else '')

        centena = centena_por_extenso if ab_c != 0 else ''
        dezena = dezena_por_extenso if ab_d != 0 else ''
        unidade = unidade_por_extenso if ab_u != 0 else ''

        spas1 = ''
        spas2 = ''

        if ab_c >= 1 and ab_d >= 1 and ab_u >= 1:
            spas1 = ', '
            spas2 = ' e '
        elif ab_c == 0 and ab_d >= 1 and ab_u >= 1:
            spas2 = ' e '
        elif ab_c >= 1 and ab_d >= 1 and ab_u == 0 or ab_c >= 1 and ab_d == 0 \
                and ab_u >= 1:
            spas1 = ' e '

        return f'{centena}{spas1}{dezena}{spas2}{unidade}.'


def main():
    # entrada de dados
    numero = int(input('Digite um número entre 0 e 999: '))

    # saída de dados junto com o processamento
    print(mostra_numero_por_extenso(numero))


if __name__ == '__main__':
    main()

```




## É vivendo e aprendendo!
# . . .