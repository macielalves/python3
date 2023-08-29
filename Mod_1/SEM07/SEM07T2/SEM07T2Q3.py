# Questão 03
# O programa analiza dois digitos de 10 a 99


def verifica_se_e_impar(n):
    if type(n) != str:
        n = str(n)
        
    n = n.lstrip('0').replace('.','').strip()
    
    if n.isnumeric():
        if len(n) < 3 and len(n) > 1:
            
            n = int(n)            
            n1 = (n % 10) % 2 != 0
            n2 = (n // 10 % 10) % 2 != 0
            
            if n1 and n2 == True:
                return 'Os dois dígitos são ímpares.'
            
            elif n1 or n2 == True:
                return 'Apenas um dígito é ímpar.'
            
            elif n1 or n2 == False:
                return 'Nenhum dígito é ímpar.'

def main():
    
    num = input('Digite um numero inteiro entre 10 a 99: ')
    print(verifica_se_e_impar(num))


if __name__=='__main__':
    main()
