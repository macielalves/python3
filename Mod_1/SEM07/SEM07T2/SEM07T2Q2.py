# Questão 02
# O programa mostra quantos caracteres pares o usuário digitou

def num_par(a):
    if type(a) != str:
        a = str(a)
    a = a.lstrip('0').replace('.','').strip()
    if a.isnumeric():
        if len(a) == 3:
            a = int(a)
            # ler se um caractere
            if len(str(a)) == 1:
                n1 = (a % 10) % 2 == 0
                #par armazena um booleano com valor 0(False) ou 1(True)
                par = n1 + 0
                print(f'{a} tem {par} dígito par')
            # ler se dois caractere
            elif len(str(a)) == 2:
                n1 = (a % 10) % 2 == 0
                n2 = (a // 10 % 10) % 2 == 0
                par = n1 + n2
                # se tiver mais de um par...
                if par > 1:
                    print(f'{a} tem {par} dígitos pares')
                    #return f'{a} tem {par} dígitos pares'#para reuso
                else:
                    print(f'{a} tem {par} dígito par')
            #ler se tres caracteres
            elif len(str(a)) == 3:
                n1 = (a % 10) % 2 == 0
                n2 = (a // 10 % 10) % 2 == 0
                n3 = (a // 100 % 10) % 2 == 0
                par = n1 + n2 + n3
                if par > 1:
                    print(f'{a} tem {par} dígitos pares')
                else:
                    print(f'{a} tem {par} dígito par')


def main():
    
    # entrada do usuário
    a = input('Digite um numero inteiro entre 100 e 999: ').strip()
    num_par(a)



if __name__=='__main__':
    main()
