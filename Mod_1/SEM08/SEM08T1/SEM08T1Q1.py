def idade(da, ma, aa, dn, mn, an):
    dias = da - dn
    meses = ma - mn
    anos = aa - an
    ## se a subtração resultar em valor negativo
    if dias < 0:
        meses -= 1
        
    if meses < 0:
        anos -= 1

    return anos

def main():
    print('Calcula quantos anos você possui!')
    dia_atual = int(input('Digite o dia atual: '))
    mes_atual = int(input('Digite o mês atual: '))
    ano_atual = int(input('Digite o ano atual: '))
    dia_nasc = int(input('Digite o dia de seu nascimento: '))
    mes_nasc = int(input('Digite o mês de seu nascimento: '))
    ano_nasc = int(input('Digite o ano de seu nascimento: '))
    print(f'Você possui {idade(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc)} anos de idade.')

if __name__ == '__main__':
    main()