def clasifica_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc < 25:
        return 'Peso normal'
    elif imc < 30:
        return 'Sobrepeso'
    elif imc < 35:
        return 'Obeso leve'
    elif imc < 40:
        return 'Obeso moderado'
    elif imc >= 40:
        return 'Obeso mórbido'
    

def main():
    peso = float(input('Digite seu peso em quilogramas(kg): '))# kg
    altura = float(input('Digite sua altura em metros(m): ')) # m
    imc = peso / altura ** 2
    print(f'Seu imc: {imc}')
    print(f'Sua classificação: {clasifica_imc(imc)}')
    

if __name__ == '__main__':
    main()