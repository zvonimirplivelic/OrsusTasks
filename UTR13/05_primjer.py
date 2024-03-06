# Napišite program koji će nacrtati službeni simbol Olimpijskih igra. Potrebno je za krugove veličine
# 50 koristiti odgovarajuće boje slijeva nadesno: plava, žuta, crna, zelena i crvena. Ispod simbola
# potrebno je zelenom bojom napisati Olimpijske igre, fontom Ariel, veličine 16.

from turtle import *

pensize(5)

color("blue")
penup()
goto(-110, -25)
pendown()
circle(50)
 
color("black")
penup()
goto(0, -25)
pendown()
circle(50)
 
color("red")
penup()
goto(110, -25)
pendown()
circle(50)
 
color("yellow")
penup()
goto(-55, -75)
pendown()
circle(50)
 
color("green")
penup()
goto(55, -75)
pendown()
circle(50)

penup()
goto(-75, -125)
write("Olimpijske igre", font=("Arial", 16, "normal"))
penup()

exitonclick()