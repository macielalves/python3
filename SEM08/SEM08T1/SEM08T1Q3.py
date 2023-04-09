def maior(n1,n2=0,n3=0,n4=0,n5=0):
    if n1 >= n2 and n1 >= n3 and n1 >= n4 and n1 >= n5:
        return n1
    elif n2 >= n1 and n2 >= n3 and n2 >= n4 and n2 >= n5:
        return n2
    elif n3 >= n1 and n3 >= n2 and n3 >= n4 and n3 >= n5:
        return n3
    elif n4 >= n1 and n4 >= n2 and n4 >= n3 and n4 >= n5:
        return n4
    elif n5 >= n1 and n5 >= n2 and n5 >= n3 and n5 >= n4:
        return n5

def menor(n1,n2=0,n3=0,n4=0,n5=0):
    if n1 <= n2 and n1 <= n3 and n1 <= n4 and n1 <= n5:
        return n1
    elif n2 <= n1 and n2 <= n3 and n2 <= n4 and n2 <= n5:
        return n2
    elif n3 <= n1 and n3 <= n2 and n3 <= n4 and n3 <= n5:
        return n3
    elif n4 <= n1 and n4 <= n2 and n4 <= n3 and n4 <= n5:
        return n4
    elif n5 <= n1 and n5 <= n2 and n5 <= n3 and n5 <= n4:
        return n5

def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())

    print(maior(n1, n2, n3, n4, n5))
    print(menor(n1, n2, n3, n4, n5))


if __name__ == '__main__':
    main()