
def main():
    soma = 0
    while True:
        try:
            num = int(input())
        except ValueError:
            print()
            continue
        else:
            if num == 0:
                break
            soma += num

    print(soma)


if __name__ == "__main__":
    main()
