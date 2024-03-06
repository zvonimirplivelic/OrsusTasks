# Napišite program koji će nacrtati pravokutnik ruba crne boje, a ispuna svijetlozelene boje. Prije
# crtanja program traži korisnika da unese duljinu i širinu.

from turtle import *

def nacrtaj_pravokutnik(duljina_pravokutnika, sirina_pravokutnika):
    fillcolor("lightgreen")
    begin_fill()

    for _ in range(2):
        forward(duljina_pravokutnika)
        left(90)
        forward(sirina_pravokutnika)
        left(90)
    end_fill()

duljina_pravokutnika = int(input("Unesite duljinu pravokutnika: "))
sirina_pravokutnika = int(input("Unesite širinu pravokutnika: "))

speed(1)
pensize(3)

nacrtaj_pravokutnik(duljina_pravokutnika, sirina_pravokutnika)

exitonclick()