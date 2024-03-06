# Napišite program koji će nacrtati kvadrat crne boje. Prije crtanja program traži korisnika da unese
# duljinu stranice kvadrata.

from turtle import *

def nacrtaj_kvadrat(duljina_stranice):
    fillcolor("black")
    begin_fill()
    for _ in range(4):
        forward(duljina_stranice)
        left(90)
    end_fill()

duljina_stranice = int(input("Unesite duljinu stranice kvadrata: "))
speed(1)
pensize(3)

nacrtaj_kvadrat(duljina_stranice)

exitonclick()