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
                if 0 == op:
                    print('0 - Fim de serviço.')
                    break
                if 1 == op:
                    print('1 - Olá. Como vai?')
                if 2 == op:
                    print('2 - Vamos estudar mais.')
                if 3 == op:
                    print('3 - Meus Parabéns!')
            else:
                print("Opção inválida.")
                continue


if __name__ == "__main__":
    main()
