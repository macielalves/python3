# Questão 01
# O programa recebe o seu nome e seu gênero e mostra uma saldação formal.


def simp_form(sexo):
    if sexo == 1:
        return 'Ilmo Sr.'

    elif sexo == 2:
        return 'Ilma Sra.'

#    else:
#       sexo = f'Erro! type {type(sexo)} requer int'
#        return sexo


def main():
    nome = input('Digite seu nome: ').strip()
    s = int(input('[1] Masculino\n[2] Feminino\nQual seu sexo: '))

    print('{} {}'.format(simp_form(s), nome.title()))


if __name__=='__main__':
    main()
