def alcanca(distancia_ha_frente):
    tartaruga = 1  # Velocidade da tartaruga em m/minutos
    lebre = 10     # Velocidade da lebre em m/minutos

    dv = lebre - tartaruga  # diferença de velocidades

    tempo_de_alcance = distancia_ha_frente / dv  # tempo em minutos

    return tempo_de_alcance


def main():
    # entrada de dados
    distancia_vantagem = float(input("Digite quantos metros a tartaruga saiu a frente da lebre: "))

    # processamento de dados
    tempo_de_alcance = alcanca(distancia_vantagem)

    # saída de dados
    print(f'A lebre alcança depois de {tempo_de_alcance:.0f} minutos')


if __name__ == "__main__":
    main()
