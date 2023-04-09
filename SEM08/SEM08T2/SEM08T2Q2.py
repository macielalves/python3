def soma_digito(n=0):
    n1 = n2 = n3 = n4 = n5 = n6 = 0
    if n != int:
        n = int(n)
    if 0 <= n < 100000:
        # soma = 0
        # n = str(n)
        # qn = len(n)
        # for t in range(0, qn):
        #     soma = int(n[t]) + soma
        n1 = n % 10
        n2 = n // 10 % 10
        n3 = n // 100 % 10
        n4 = n // 1000 % 10
        n5 = n // 10000 % 10
        n6 = n // 100000 % 10
        soma = n1 + n2 + n3 + n4 + n5 + n6
        return soma

    else:
        return -1


n = int(input())
print(soma_digito(n))
