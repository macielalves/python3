# Escreva um programa que gere uma sequência a cada 10 até 1000
def n_sequencia(start, stop, step=1):
    acumuladora = ''
    for i in range(start, stop, step):
        acumuladora += str(i+step) + (', ' if i != (stop-step) else '.')

    return acumuladora


string_acumulada = n_sequencia(0, 1000, 10)
print(string_acumulada)
