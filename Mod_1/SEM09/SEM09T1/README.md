># semana 09

## Meu código de destaque:

```python
## Código presente no arquivo SEM09T1Q4.py

# Entrada de dados
a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
c = int(input('Digite um terceiro número inteiro: '))

# atribuindo zero as variáveis
segundo_valor = terceiro_valor = 0

# processamento
segundo_valor = abs(b - a)
terceiro_valor = abs(c - a)
valor = segundo_valor if segundo_valor < terceiro_valor else terceiro_valor

# saída de dados
print(f'A menor diferença foi de {valor}')

```