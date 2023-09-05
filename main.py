import Mod_2

with open("logo.txt", "r") as logo:
    print("Desenvolvido por:\n", logo.read(), sep="")
    logo.close()

s1 = Mod_2.main.Semaforo()
s1.ligar()
