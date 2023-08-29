def main():
    nome = input().strip()
    op = input().strip()
    if op == '1':
       cg = input().strip()
       nome = nome + cg

    print(conta_letra(nome))


#contanto que a definição fique antes do inicializador funciona
def conta_letra(n):
    n = n.replace(' ', '')
    count = len(n)
    return count


if __name__=='__main__':
    main()
