#Q1
def eh_vogal(a):
    return a.strip().lower() in ('aeiou')

#Q2
def eh_letra(letra):
    return eh_vogal(letra) or eh_consoante(letra)  

#Q3
def eh_consoante(b):
    return b.strip().lower() in ('bcdfghjklmnpqrstvwxyz')  


def eh_numero(n):
    return n.strip() in ('0123456789')
    
def eh_letra_ou_numero(c):
    return eh_letra(c) or eh_numero(c)

def eh_simbolo(s):
    return eh_letra_ou_numero(s) == False

def main():
    texto = str(input('Digite um caractere: '))
    
    print(f'O caractere digitado é um simbolo? {eh_simbolo(texto)}')
    
if __name__ == '__main__':
    main()
