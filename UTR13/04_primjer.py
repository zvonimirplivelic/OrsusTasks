# Napišite program koji će nacrtati pismo (kuvertu) crne boje koja se sastoji od kvadrata i trokuta.
# Prije crtanja program traži korisnika da unese duljinu stranice kvadrata. Za dijagonale i gornji dio
# kvadrata potrebno je crtati u ovisnosti duljine stranice kvadrata.

from turtle import *
from math import sqrt

def nacrtaj_kvadrat(duljina_stranice):
    for _ in range(4):
        forward(duljina_stranice)
        left(90)

duljina_stranice = int(input("Unesite duljinu stranice kvadrata: "))
speed(1)
pensize(3)

nacrtaj_kvadrat(duljina_stranice)

left(45)
forward(duljina_stranice * sqrt(2))
left(135)
forward(duljina_stranice)
left(135)
forward(duljina_stranice * sqrt(2))
left(135)
forward(duljina_stranice)
left(45)
forward(duljina_stranice * sqrt(2) / 2)
left(90)
forward(duljina_stranice * sqrt(2) / 2)

exitonclick()