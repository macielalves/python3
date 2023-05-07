# Quando que a poupança dobrará o depósito inicial

def main():
    # Valor Principal
    p = float(input('Digite o valor do depósito inicial: '))
    juros = float(input('Digite a taxa de juros ao ano da poupança: '))

    # Converter para fração de 100 ()
    juros /= 100

    ##
    tempo = 0
    dobro = p * 2
    anos = ''

    while p <= dobro:
        # Condições para formatação de saída
        if tempo >= 0:
            anos = 'início'
            if tempo == 1:
                anos = f'{tempo} ano'
            elif tempo > 1:
                anos = f'{tempo} anos'

        # Processar juros compostos (poupança)
        p = p + juros * p
        tempo += 1

        # print(f"{anos:^8} | {p:^8.2f}")  # Formatação principal
        print(tempo)
        print(f'{p:.2f}')


if __name__ == "__main__":
    main()
