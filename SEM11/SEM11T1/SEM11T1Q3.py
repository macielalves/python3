def main():
    # definição das variáveis como 2, o porquê é simples, o único valor que é maior é 3
    maior = 0
    menor = 0
    # tranca no primeiro valor de entrada
    trava = 1

    while True:
        numbers = abs(int(input('Digite qualquer número e se quiser parar é só digitar 0: ')))

        # é maior que zero e maio que maior

        if 0 < numbers > maior:
            maior = numbers

        # Testa se o valor digitado é maior que zero e se for ele pega esse valor como base para ser o menor
        if numbers > 0 and trava == 1:
            menor = numbers
            trava = 0

        if menor > numbers != 0:
            menor = numbers

        elif numbers == 0:
            break

    print('O maior', maior)
    print('O menor', menor)


if __name__ == "__main__":
    main()
