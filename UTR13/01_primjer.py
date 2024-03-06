# Napišite program koji će koristeći Turtle mode nacrtati jednakostranični trokut ruba crne boje, a
# ispuna svijetlozelene boje. Prije crtanja program traži korisnika da unese duljinu stranice trokuta.

from turtle import *

def nacrtaj_trokut(duljina_stranice):
    fillcolor("lightgreen")
    begin_fill()
    for _ in range(3):
        forward(duljina_stranice)
        left(120)
    end_fill()

duljina_stranice = int(input("Unesite duljinu stranice trokuta: "))
speed(1)
pensize(3)

nacrtaj_trokut(duljina_stranice)

exitonclick()
# done()