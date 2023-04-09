def media_final(nt1, nt2=0, nt3=0, mde=0):
    mf = (nt1 + nt2*2 + nt3*3 + mde) / 7
    if mf > 10:
        mf = 10
    elif mf < 0:
        mf = 0
    return mf


def conceito(mf):
    mf = float(mf)
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


def estatus(txt):
    txt = str(txt).strip()
    if txt == 'A' or txt == 'B' or txt == 'C':
        return 'Aprovado'
    elif txt == 'D' or txt == 'E':
        return 'Reprovado'


n_matricula = input().strip()
nota1 = float(input().strip())# 1º nota
nota2 = float(input().strip())# 2º nota
nota3 = float(input().strip())# 3º nota
media_exercicios = float(input().strip())
mf = media_final(nota1, nota2, nota3, media_exercicios)
conceito = conceito(mf)

print(n_matricula)
print(f'{mf:.2f}')
print(conceito)
print(estatus(conceito))
