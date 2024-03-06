# Napišite program koji će koristeći numinput funkciju (funkcija za prikazivanje dijaloškog okvira za
# unos) za unos broja stranica mnogokuta. Potrebno je za mnogokut uzeti rub crne boje, a ispuna
# svijetlozelene boje.
from turtle import *

def nacrtaj_mnogokut(broj_stranica):
    pendown()
    begin_fill()
    color("black", "lightgreen")  
    for _ in range(broj_stranica):
        forward(50)  
        right(360 / broj_stranica)
    end_fill()
    penup()

broj_stranica = numinput("Generiranje mnogokuta:", "Molim vas da unesete broj stranica mnogokuta", 5, 3)

broj_stranica = int(broj_stranica)
speed(2)
penup()

goto(-50, -50)

nacrtaj_mnogokut(broj_stranica)

exitonclick()
