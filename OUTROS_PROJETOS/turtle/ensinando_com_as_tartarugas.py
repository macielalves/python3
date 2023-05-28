from turtle import *
import random

random.seed()


def planeta(raio=100, cor='black', cheio=False):
    """Necessita de importar o módulo turtle.py"""
    pendown()
    if cheio:
        begin_fill()
        color(cor)
    numero_lados = 100  # Número de lados do polígono

    # Desenho do círculo
    angulo = 360 / numero_lados
    for _ in range(numero_lados):
        forward(raio * angulo / 360)
        left(angulo)

    if cheio:
        end_fill()
    penup()


def quadrado(a=100, cor='black', cheio=False):
    pendown()
    if cheio:
        begin_fill()
        color(cor)
    for i in range(4):
        forward(a)
        left(90)

    if cheio:
        end_fill()
    penup()


# uma função para desenhar uma estrela
def draw_star(star_size, star_colour):
    color(star_colour)
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(star_size)

    end_fill()
    penup()


def gera_cores(n=1):
    num_hexa = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    sorteia_cores = []

    for cor in range(n):
        nova_cor = ''
        for lonely in range(6):
            a = random.randrange(16)
            nova_cor += num_hexa[a]

        sorteia_cores.append('#' + nova_cor)

    return sorteia_cores


def galaxia(n):
    star_colour = gera_cores(10)
    mover_aleatorio()
    for star in range(n):
        penup()
        left(random.randint(-180, 180))
        forward(random.randint(6, 26))
        pendown()

        draw_star(2, random.choice(star_colour))


def mover_aleatorio():
    penup()
    setpos(random.randint(-400, 400), random.randint(-400, 400))
    pendown()


def main():
    speed(11)
    bgcolor('black')

    for galax in range(6):
        mover_aleatorio()
        quadrado(random.randint(100, 200), random.choice(gera_cores(6)))
        mover_aleatorio()
        galaxia(36)

    for i in range(random.randrange(6, 16)):
        for star in range(random.randint(0, 4)):
            star_size = random.randint(16, 36)
            star_colour = 'white'

            draw_star(star_size, star_colour)
            mover_aleatorio()

        estilo_frufru = random.choice(gera_cores(1))
        tamanho_do_planeta = random.randrange(206, 406, 26)

        planeta(tamanho_do_planeta, estilo_frufru, True)
        mover_aleatorio()

    hideturtle()
    done()


if __name__ == "__main__":
    main()

# # isso vai desenhar uma estrela cinza em um fundo azul-escuro
# color("WhiteSmoke")
# bgcolor("MidnightBlue")
#
# pendown()
# begin_fill()
#
# # desenha a forma da estrela
# for side in range(5):
#     left(144)
#     forward(50)
#
#
# end_fill()
# penup()
#
#
# forward(100)
# done()


# # uma função para desenhar uma estrela
# def drawStar():
#     pendown()
#     begin_fill()
#     for side in range(5):
#         left(144)
#         forward(50)
#
#     end_fill()
#     penup()
#
#
# color("WhiteSmoke")
# bgcolor("MidnightBlue")
#
#
# drawStar()
# forward(100)
# drawStar()
# left(120)
# forward(150)
# drawStar()
#
#
# hideturtle()
# done()
