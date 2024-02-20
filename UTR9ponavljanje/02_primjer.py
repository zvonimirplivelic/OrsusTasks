# Napišite glavni program koji učitava dva broja. Potrebno je napisati glavnu funkciju
# racunajGlavna koja prima ta dva broja kao parametre te ih zbraja. Na temelju rezultata zbroja ta
# dva broja unutar glavne funkcije potrebno je pozvati dvije unutarnje funkcije: parnaUnutarnja i
# neparnaUnutarnja. Funkcija parnaUnutarnja vraća rezultat matematičkog izraza (a-b) 2 , a funkcija
# neparnaUnutarnja vraća rezultat matematičkog izraza izraza korijen (a 2 +b 2 ).

from math import sqrt

def racunajGlavna(main_a, main_b):
    def parnaUnutarnja(in_a, in_b):
        return (in_a - in_b) ** 2

    def neparnaUnutarnja(in_a, in_b):
        return sqrt(in_a ** 2 + in_b ** 2)
    
    rezultat = int(main_a + main_b)

    if rezultat % 2 == 0:
        rez_funkcije = float(parnaUnutarnja(main_a, main_b))
    else:
        rez_funkcije = float(neparnaUnutarnja(main_a, main_b))

    return rez_funkcije

prvi_broj = int(input("Molim vas da unesete prvi broj: "))
drugi_broj = int(input("Molim vas da unesete drugi broj: "))

print(f"Vrijednost koju program vraća je: {racunajGlavna(prvi_broj, drugi_broj)}")