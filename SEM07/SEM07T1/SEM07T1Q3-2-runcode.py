def junta_letra(frase):
    return frase.replace(' ', '').strip()


def sinal(cor):
    cor = junta_letra(cor)
    if cor[0:4].upper() in ('VERMELHO', 'VERM','E', 'VM', 'ERM'):# vermelho
        return 'Pare'
    
    elif cor[0:4].upper() in ('VERDE', 'VERD', 'V', 'VD', 'ERD'):# verde
        return 'Siga'
        
    elif cor[0:4].upper() in ('AMARELO', 'AMAR', 'A', 'AM', 'AMA'):# amarelo
        return 'Atenção'

    else:
        return 'Não entendi'
    
  
print(sinal(input()))
        
