import random

# Lista de cumprimentos
cumprimentos = [
    "Olá!",
    "Oi!",
    "E aí?",
    "Como vai?",
    "Bom dia!",
    "Boa tarde!",
    "Boa noite!"
]

# Lista de adjetivos
adjetivos = [
    "amigável",
    "incrível",
    "maravilhoso",
    "fantástico",
    "brilhante",
    "gentil",
    "espetacular",
    "notável"
]

# Lista de nomes de usuário
nomes = [
    "amigo",
    "campeão",
    "chefe",
    "companheiro",
    "parceiro",
    "herói",
    "gênio",
    "mestre"
]


# Função para gerar um cumprimento personalizado
def gerar_cumprimento(nome, adjetivo):
    cumprimento = random.choice(cumprimentos)
    return f"{cumprimento} {nome}! Você é {adjetivo}."


# Função para modificar as preferências do usuário
def modificar_preferencias():
    while True:
        print("=== Menu de Preferências ===")
        print("1. Adicionar adjetivo")
        print("2. Remover adjetivo")
        print("3. Sair do menu de preferências")
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            adjetivo = input("Digite o adjetivo que deseja adicionar: ")
            adjetivos.append(adjetivo)
            print(f"Adjetivo '{adjetivo}' adicionado com sucesso!")
        elif opcao == "2":
            print("=== Adjetivos disponíveis ===")
            for i, adjetivo in enumerate(adjetivos, start=1):
                print(f"{i}. {adjetivo}")
            indice = int(input("Digite o número do adjetivo que deseja remover: ")) - 1
            if indice >= 0 and indice < len(adjetivos):
                adjetivo_removido = adjetivos.pop(indice)
                print(f"Adjetivo '{adjetivo_removido}' removido com sucesso!")
            else:
                print("Opção inválida!")
        elif opcao == "3":
            break
        else:
            print("Opção inválida!")


# Função principal do programa
def main():
    nome_usuario = input("Digite seu nome de usuário: ")
    print()
    print("Bem-vindo(a) ao Gerador de Cumprimentos!")
    print()
    print("=== Menu Principal ===")
    print("1. Gerar cumprimento")
    print("2. Modificar preferências")
    print("3. Sair do programa")

    while True:
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            adjetivo = random.choice(adjetivos)
            cumprimento = gerar_cumprimento(nome_usuario, adjetivo)
            print(cumprimento)
        elif opcao == "2":
            modificar_preferencias()
        elif opcao == "3":
            print("Até mais!")
            break
        else:
            print("Opção inválida!")


# Executa o programa
main()
