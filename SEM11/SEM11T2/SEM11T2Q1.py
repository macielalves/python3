
def main():
    soma = 0
    while True:
        try:
            num = int(input())
        except ValueError:
            print('Digite um valor válido!')
            continue
        else:
            if num == 0:
                break
            soma += num

    if soma != 0:
        print(soma)


if __name__ == "__main__":
    main()
