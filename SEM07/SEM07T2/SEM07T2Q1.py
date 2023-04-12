# Questão 01
# O programa pergunta ao usuário seu nome e seu estado civil e caso casado\
# pergunta o nome do cônjuge e mostra o total de caracteres do(s) nome(s) digitado

def questionario():#   def main():
    nome = input('Digite seu nome: ').strip()
    op = input('[1]Casado(a)\n[2]Solteiro(a)\nEscolha uma opção: ').strip()
    if op == '1':
        cg = input('Digite o nome do cônjuge: ').strip()
        nome = nome + cg
        print('Seus nomes possuem %d letras no total' % conta_letra(nome))

    if op == '2':
        print('Seu nome possui %d letras' % conta_letra(nome))


#função antes do inicializador
def conta_letra(n):
    n = n.replace(' ', '')
    count = len(n)
    return count


if __name__=='__main__':
    questionario()#    main()
