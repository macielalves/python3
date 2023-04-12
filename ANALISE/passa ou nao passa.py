n_da_matricula = input()
n1 = float(input())
n2 = float(input())
n3 = float(input())
media = float(input())
media_final: float = (n1+ n2 * 2 + n3 * 3 + media) / 7

if media_final >= 9.0:
    print(f'{n_da_matricula}\n{media_final:.2f}\nA\nAprovado')
elif media_final >= 7.5 and media_final < 9.0:
    print(f'{n_da_matricula}\n{media_final:.2f}\nB\nAprovado')
elif media_final >= 6.0 and media_final <7.5:
    print(f'{n_da_matricula}\n{media_final:.2f}\nC\nAprovado')
elif media_final >= 4.0 and media_final < 6.0:
    print(f'{n_da_matricula}\n{media_final:.2f}\nD\nReprovado')
else:
    print(f'{n_da_matricula}\n{media_final:.2f}\nE\nRprevovado')

