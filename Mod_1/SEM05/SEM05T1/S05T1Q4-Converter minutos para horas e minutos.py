input_time_min = int(input('Insira um valor em minutos: '))

def horas_minutos(minut):
    h = minut // 60
    m = minut % 60
    return h, m

def main():
    h, m = horas_minutos(input_time_min)
    # horas = horas_minutos(input_time_min)[0]
    # minutos = horas_minutos(input_time_min)[1]
    print(f'{input_time_min} minutos é equivalente a {h} horas e {m} minutos \033[5;32m{h}:{m}\033[0m')#\033[5;32m -> o 5 faz piscar o texto e o 32 é a cor

if __name__ == '__main__':
    main()
