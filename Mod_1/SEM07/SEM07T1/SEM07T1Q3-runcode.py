def sinal(cor):
    if cor[0].upper() == 'V':# verde
        print('Siga')
        
    elif cor[0].upper() == 'A':
        print('Atenção')
        
    elif cor[-1].upper() == 'E':# vermelho
        print('Pare')

sinal(input())
        
