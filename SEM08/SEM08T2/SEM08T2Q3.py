def edivisivel(n):
    if n >= 0:
        if n % 3 == 0 or n % 5 == 0:
            t1=t2=t3=''
            if n % 3 == 0 :
                t1 = 'FIZZ'
            if n % 5 == 0:
                t2 = 'BUZZ'
            if n % 3 == 0 and n % 5 == 0:
                t3 = t1 + t2
                t1 = t2 = ''

            return t1 + t2 + t3
        else:
            return n


n = int(input())
print(edivisivel(n))