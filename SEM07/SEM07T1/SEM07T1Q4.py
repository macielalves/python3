# Questão 04
# O programa analizará um caractere digitado (caso ele conheça;) e mostrará se é consoante, vogal, número ou símbolo


def verifica_caractere(c):
    if len(c) == 1:
        if c.isascii():
            # verifica se é numérico
            if c.isalnum():
                if c.lower() in ('aeiou'):
                    return 'vogal'
            
                elif c.lower() in ('bcdfghjklmnpqrstvwxyz'):
                    return 'consoante'
            
                elif c.isnumeric() or c.isdigit():
                    return 'número'
            
            # caso ainda for ascii deve ser um símbolo
            return 'símbolo'
            
        elif str(ord(c)).isnumeric():
                return 'símbolo'
    ### para que a função abaixo funcione substitua a charp (#) no início da linha 24 e 27 por espaço vazio
    ### após comente as linhas 28, 29 e 30.
#   return 'Tente colocar somente um caractere e tente novamente'

def main():
#   print(verifica_caractere(input('Digite um caractere: ').strip()))
    caractere = str(input('Digite um caractere: ')).strip()
    if len(caractere) == 1:
        print(verifica_caractere(caractere))


if __name__=='__main__':
    main()

### Tem mais comentários que funções :)
