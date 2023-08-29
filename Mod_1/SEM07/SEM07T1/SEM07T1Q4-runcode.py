## Questão 04
### O programa analizará um caractere digitado (caso ele conheça;) e mostra o resultado
def verifica_caractere(c):
    if len(c) == 1:
        if c.isascii():
            ### verifica se é numérico
            if c.isalnum():
                if c.lower() in ('aeiou'):
                    return 'vogal'
            
                elif c.lower() in ('bcdfghjklmnpqrstvwxyz'):
                    return 'consoante'
            
                elif c.isnumeric() or c.isdigit():
                    return 'número'
            
            ### caso ainda for ascii deve ser um símbolo    
            return 'símbolo'            
            
        elif str(ord(c)).isnumeric():
                return 'símbolo ascii fora dos 7-bits'

        
print(verifica_caractere(input().strip()))
