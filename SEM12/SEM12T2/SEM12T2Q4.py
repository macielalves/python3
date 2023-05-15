def verificar_primo(numero):
    if numero < 2:  # não inclui os números negativos e nem 0 ou 1
        return False

    for i in range(2, int(numero ** 0.5) + 1):  # numero ** 0.5 == raiz_quadrada(numero)
        if numero % i == 0:  # verifica se o valor no intervalo de 2 até a raiz do número mais 1 for igual a 0
            return False  # Falso se divisível por um número que não seja 1 ou ele mesmo

    return True


def main():
    numero = int(input("Digite um número inteiro: "))

    if verificar_primo(numero):  # como if responde a True e False assim posso usar a saída da função como condição
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")


if __name__ == "__main__":
    main()
