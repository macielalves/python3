# lista de letras para criptografar
alfabeto = "abcdefghijklmnopqrstuvwxyz"

# a chave secreta é a entrada de dados do usuário
chave = int(input('Digite uma chave para criptografia: '))

letra = input("Por favor, entre com uma letra para criptografar: ")

# encontre a posição da letra em alfabeto
# exemplo: 'a' está na posição 0, 'e está na posição 4, etc.
posicao = alfabeto.find(letra)

# some a chave secreta para encontrar a podição da letra criptografada
# % 26 significa 'volte para 0 quando você chegar no 26'
nova_posicao = (posicao + chave) % 26

# a letra criptografada está no alfabeto na nova posição
letraCriptografada = alfabeto[nova_posicao]

print("Sua letra criptografada é", letraCriptografada)
