lado = float(input('Digite o valor correspondente ao lado do quadrado: '))

def area_do_quadrado(a):
    return a ** 2

def perimetro_do_quadrado(p):
    return 2 * (p + p)#p ira corresponder ao lado

print(f'A área do quadrado é {area_do_quadrado(lado):10.4f}')
print(f'E o perimetro do quadrado é {perimetro_do_quadrado(lado):10.4f}')
