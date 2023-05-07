def main():
    while True:
        print(
            'OPÇÕES:',
            '1 - SAUDAÇÃO',
            '2 - BRONCA',
            '3 - FELICITAÇÃO',
            '0 - FIM', sep='\n'
        )
        try:
            op = int(input())
        except ValueError:
            print('Digite um valor válido!')
        else:
            if op in (0, 1, 2, 3):
                if op in 0:
                    print('Fim de serviço.')
                    break
                if op in 1:
                    print('Olá. Como vai?')
                if op in 2:
                    print('Vamos estudar mais.')
                if op in 3:
                    print('Meus Parabéns!')
            else:
                print("Opção inválida.")
                continue


if __name__ == "__main__":
    main()
