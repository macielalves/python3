# Questão 02
# O programa, se o usuário digirar


def num_par(a):
    if type(a) != str:
        a = str(a)
    a = a.lstrip('0').replace('.','').strip()
    if a.isnumeric():
        # converte para inteiro
        if len(a) < 6:
            par = 0
            a = int(a)
            
            # ler se um caractere
            if len(str(a)) == 1:
                n1 = (a % 10) % 2 == 0
                #par armazena um booleano com valor 0(False) ou 1(True)
                par = n1
                
            # ler se dois caractere
            elif len(str(a)) == 2:
                n1 = (a % 10) % 2 == 0
                n2 = (a // 10 % 10) % 2 == 0
                par = n1 + n2

            #ler se tres caracteres
            elif len(str(a)) == 3:
                n1 = (a % 10) % 2 == 0
                n2 = (a // 10 % 10) % 2 == 0
                n3 = (a // 100 % 10) % 2 == 0
                par = n1 + n2 + n3

            print(par)
                

def main():
    #entrada do usuário
    a = input().strip()
    num_par(a)


if __name__=='__main__':
    main()
