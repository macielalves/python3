def simp_form(sexo):
    if sexo == 1:
        sexo = 'Ilmo Sr.'
    elif sexo == 2:
        sexo = 'Ilma Sra.'
    else:
        sexo = ''
    return sexo

nome = input().strip()
s = int(input())

print('{} {}'.format(simp_form(s), nome.title()))
