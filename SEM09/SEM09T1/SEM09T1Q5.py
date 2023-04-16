n = int(input())
resto = n % 5
if resto == 0:
    print(9 * n + 7)
elif resto == 1:
    print('par' if n % 2 == 0 else 'ímpar')
elif resto == 2:
    print(5 * n ** 2 - 3 * n + 42)
elif resto == 3:
    print(n // 10)
elif resto == 4:
    print(n ** 2)
