def criptografa(letra, chave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    posicao = alfabeto.find(letra)
    nova_posicao = (posicao + chave) % len(alfabeto)
    nova_letra = alfabeto[nova_posicao]
    return nova_letra


def descriptografa(letra, chave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    posicao = alfabeto.find(letra)
    nova_posicao = (posicao - chave) % len(alfabeto)
    nova_letra = alfabeto[nova_posicao]
    return nova_letra


print(criptografa('a', 3))

print(criptografa('d', 7))
print(criptografa('x', 4))

for i in 'omqemd':
    print(descriptografa(i, 12), end='')
