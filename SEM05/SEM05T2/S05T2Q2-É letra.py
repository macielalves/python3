def eh_vogal(a):
    return a.strip().lower() in ('aeiou')

def eh_consoante(b):
    return b.strip().lower() in ('bcdfghjklmnpqrstvwxyz')

def eh_letra(letra):
    return eh_vogal(letra) or eh_consoante(letra)    
    
def main():
    letra = str(input('Digite um caractere: '))
    print(f'O caractere digitado é letra: {eh_letra(letra)}')
    
if __name__ == '__main__':
    main()
