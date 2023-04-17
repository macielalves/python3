b = int(input('Digite o valor da base de um retângulo: '))
h = int(input('Digite o valor da altura de um retângulo: '))

print(f'O perímetro e área são:\n{2*b + 2*h} - {b * h}' if b != h else
      'QUADRADO')
