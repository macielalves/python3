# Questão 03
# O programa opera como sinaleiro;
# Caso digite 'verde' ou uma parte 'verd' que identifique a cor ele mostra lhe informa uma ação.

def junta_letra(frase):
    # a função replace substitui os espaços por vazio
    return frase.replace(' ', '').strip()


def sinal(cor):
    cor = junta_letra(cor)

    # condição para setar o tamanho da letra no operador de formatação "[:]"
    if len(cor) < 5:
        t = len(cor)
        up = cor[0:t].upper()

    else:
        up = cor.upper()
        
    if up in ('VERM','E', 'VM', 'ERM') or up == "VERMELHO":
        return 'Pare'
    
    elif up in ('VERD', 'V', 'VD', 'ERD') or up == "VERDE":
        return 'Siga'

    elif up in ('AMAR', 'A', 'AM', 'AMA') or up == "AMARELO":
        return 'Atenção'
    
#    ### +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ###
#    elif up == 'VER':
#        if input('Você quis dizer vermelho?(S/n) ').upper() in ('S', 'SIM', 'Y', 'YES'):
#           return sinal('VERMELHO')
           
#        input('Então é verde! ENTER para continuar...')
#        return sinal('VERDE')
#    ### +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ###
#    else:
#        return 'Não entendi!'

    
def main():
    print('("V" é verde; "A" é amarelo; "E" é vermelho)', end=': ')
    # print lê a função sinal que chama input, input retorna uma dado para função e função retorna um valor para print e print faz a mágica.
    print(sinal(input()))


if __name__ == '__main__':
    main()
