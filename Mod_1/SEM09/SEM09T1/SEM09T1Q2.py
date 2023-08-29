# questão 2 da atividade 1 da semana 9
n0 = int(input('Digite um número inteiro: '))
n1 = int(input('Digite outro número inteiro: '))
op = int(input('Escolha uma das operações abaixo:\
               \n[1]-Soma\n[2]-Subtração\n[3]-Múltiplicação\n[4]-Divisão\
                   \nDigite o número correspondente da operação: '))

if op == 1:
    print(f'A soma dos termos é {n0 + n1}')
elif op == 2:
    print(f'A subtração dos termos é {n0 - n1}')
elif op == 3:
    print(f'A múltiplicação dos termos é {n0 * n1}')
elif op == 4 and n1 != 0:
    print(f'A divisão dos termos é {n0 / n1:.2f}')
else:
    raise TypeError('Digite somente valores reais e escolha entre 1 e 4')
