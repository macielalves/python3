# questão 2 da atividade 1 da semana 9
n0 = int(input())
n1 = int(input())
op = int(input())

if op == 1:
    print(n0 + n1)
elif op == 2:
    print(n0 - n1)
elif op == 3:
    print(n0 * n1)
elif op == 4 and n1 != 0:
    print(f'{n0 / n1:.2f}')
else:
    raise TypeError('Digite somente valores reais e escolha entre 1 e 4')
