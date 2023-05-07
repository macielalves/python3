def main():
    soma = 0
    termos = 0

    while True:
        num = abs(int(input()))
        if num != 0:
            termos += 1
        else:
            if termos == 0:
                termos = 1  # :)
            break

        soma += num

    # Processamento da média
    media = soma / termos
    if media != 0:
        print(f'{media:.2f}')


if __name__ == "__main__":
    main()
