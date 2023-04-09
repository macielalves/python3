def media_final(nt1=0, nt2=0, nt3=0, mde=0):
    return float(f'{(nt1 + nt2*2 + nt3*3 + mde) / 7 :.2f}')


def conceito(mf=0):
    if mf >= 9.0:
        return 'A'
    elif mf >= 7.5 < 9.0:
        return 'B'
    elif mf >= 6.0 < 7.5:
        return 'C'
    elif mf >= 4.0 < 6.0:
        return 'D'
    elif mf < 4.0:
        return 'E'


def estatus(txt='Estude!'):
    if txt == 'A' or txt == 'B' or txt == 'C':
        return 'Aprovado'
    elif txt == 'D' or txt == 'E':
        return 'Reprovado'


n_matricula = input().strip()
nota1 = float(input())# 1º nota
nota2 = float(input())# 2º nota
nota3 = float(input())# 3º nota
media_exercicios = float(input())
mf = media_final(nota1, nota2, nota3, media_exercicios)
conceito = conceito(mf)

print(n_matricula)
print(mf)
print(conceito)
print(estatus(conceito))
