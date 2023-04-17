n = int(input('Digite um número inteiro: '))
resto = n % 5
if resto == 0:
    print(f'{9 * n + 7} é o resultado da equação 9n + 7 onde n é o valor \
        digitado')
elif resto == 1:
    print(f"O valor digitado é {'par' if n % 2 == 0 else 'ímpar'}")
elif resto == 2:
    print(f'{5 * n ** 2 - 3 * n + 42} é o resultado da equação 5n² - 3n + 42, \
        onde n é o valor lido')
elif resto == 3:
    print(f'{n // 10} é resultado da divisão inteira do valor digitado \
        por dez')
elif resto == 4:
    print(f'{n ** 2} o quadrado do valor digitado')
