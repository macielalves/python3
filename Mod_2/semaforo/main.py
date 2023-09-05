from semaforo import Semaforo
import sys
import os


class Color:
    warning = "\033[43m"+"\033[1m"+"\033[30m"
    success = "\033[42m"+"\033[1m"+"\033[30m"
    error = "\033[41m"+"\033[1m"+"\033[30m"
    clear = "\033[0m"
    green = os.system("color a0")
    cls = os.system("cls")





LOGO = f'''
Desenvolvido por:
   _______     ______     ________      ________     ______  __________   ____
  /     \\ \\   /    \\ \\   /       \\ \\   /  __  \\ \\   /___/_/ |   _____|_| |  | |
 |       \\_\\_/      | | |   ___   | | |  / /\\__|_| |   | |  |  | |       |  | |
 |                  | | |  / / \\  | | |  | |       |   | |  |  |_|___    |  | |
 |    |\\      /|    | | |  |_|_|  | | |  | |       |   | |  |   ___|_|   |  | |
 |    | \\    / |    | | |   ___   | | |  | | ____  |   | |  |  | |       |  | |
 |    | |\\__/_/|    | | |  | | |  | | |  \\_\\/  | | |   | |  |  |_|_____  |  |_|______
 |____|_|      |____|_| |__|_| |__|_|  \\______/_/  |___|_|  |________|_| |_________|_|
 Maciel Alves Pereira
'''

cores = Color()

s1 = Semaforo()
s1.ligar()


def log_semaforo(string):
    if "verde" in string:
        os.system("cls")
        print(os.getcwd())
        return f"{cores.success + string + cores.clear}"
    elif "amarelo" in string:
        os.system("cls")
        return f"{cores.warning + string + cores.clear}"
    elif "vermelho" in string:
        os.system("cls")
        return f"{cores.error + string + cores.clear}"


desligar = False
while not desligar:
    for _ in range(6):
        print(log_semaforo(s1.luz_atual))
        s1.gerenciar_tempo()

    if input("Deseja continuar? (S/n): ").strip().upper() == "N":
        desligar = True

print(LOGO)
