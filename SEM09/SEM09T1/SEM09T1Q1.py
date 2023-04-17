# questão 1 da atividade 1 da semana 9
n1 = int(input('Digite um valor numérico: '))
n2 = int(input('Digite outro valor numérico: '))
n3 = int(input('Dite um terceiro valor numérico: '))
if n1 == n2 == n3:
    print('Todos os valores são iguais')
elif n1 != n2 and n1 != n3 and n2 != n3:
    print('Todos os valores são diferentes')
else:
    print('Existem dois valores iguais e um diferente')
