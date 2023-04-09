def soma5ou8(n=0):
    if n % 2 == 0:
        n += 5
    elif n % 2 == 1:
        n += 8
    return n


n = int(input())
print(soma5ou8(n))
