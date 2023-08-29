a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
c = int(input('Digite um terceiro número inteiro: '))

segundo_valor = terceiro_valor = 0

segundo_valor = abs(b - a)
terceiro_valor = abs(c - a)
valor = segundo_valor if segundo_valor < terceiro_valor else terceiro_valor

print(f'A menor diferença foi de {valor}')
