def eh_vogal(a):
    return a.strip().lower() in ('aeiou')
    
def main():
    letra = str(input('Insira um caractere: '))
    print(f'O caractere digitado é vogal: {eh_vogal(letra)}')
    
if __name__ == '__main__':
    main()
