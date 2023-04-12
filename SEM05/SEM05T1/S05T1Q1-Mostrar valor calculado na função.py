print('Função 2a + 5b - c')
n1 = int(input('Digite um valor para a: '))
n2 = int(input('Digite uma valor pra b: '))
n3 = int(input('Digite um valo para c: '))

def calcular(a, b, c):
    return 2 * a + 5 * b - c

print(f'O valor resultante para a função é {calcular(n1, n2, n3)}')
