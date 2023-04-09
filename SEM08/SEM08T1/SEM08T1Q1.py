def idade(da, ma, aa, dn, mn, an):
    dias = da - dn
    meses = ma - mn
    anos = aa - an

    if dias < 0:
        meses -= 1
        
    if meses < 0:
        anos -= 1

    return anos

def main():
    dia_atual = int(input())
    mes_atual = int(input())
    ano_atual = int(input())
    dia_nasc = int(input())
    mes_nasc = int(input())
    ano_nasc = int(input())
    print(idade(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc))

if __name__ == '__main__':
    main()