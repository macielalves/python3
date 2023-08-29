# Questão 01
# O programa pergunta ao usuário seu nome e seu estado civil e caso casado\
# pergunta o nome do cônjuge e mostra o total de caracteres do(s) nome(s) digitado
def conta_letra(n='0'):
    n = n.replace(' ', '').strip()
    count = len(n)
    return count

def simp_form(n='0', x='2', nn = '0'):
    n_letra = conta_letra(n)
    if x == '2':
        return n_letra
    elif x == '1':
        n_letra = n_letra + conta_letra(nn)
        return n_letra
    else:
        return 0


def main():
    conjuge = '0'
    nome = input('Digite seu nome: ')# .strip()
    op = input('[1]Casado\n[2]Solteiro\nQual seu estado civil?: ')# .strip()
    if op == '2':
        conjuge = input('Digite o nome do cônjuge: ')
    print(simp_form(nome, op, conjuge))


if __name__=='__main__':
    main()
