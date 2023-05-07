def main():
    soma = 0
    termos = 0

    while True:
        num = abs(int(input('Digite um número inteiro: ')))
        if num != 0:
            termos += 1
        else:
            if termos == 0:
                termos = 1  # :)
            break

        soma += num

    # Processamento da média
    media = soma / termos

    print(f'{media:.2f}')


if __name__ == "__main__":
    main()
