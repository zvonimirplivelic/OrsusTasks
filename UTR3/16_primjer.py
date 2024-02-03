# Napišite program koji će učitati broj N koji predstavlja proizvoljan unos temperatura.
# Nakon toga potrebno je ispisati prosjek temperatura iznad 0
# i posebno prosjek temperatura ispod 0 stupnjeva

broj_temperatura = int(input("Unesite koliko očitanja temperature želite unijeti: "))
broj_pozitivnih_unosa = 0
broj_negativnih_unosa = 0

suma_pozitivnih_temperatura = 0
suma_negativnih_temperatura = 0

for i in range (broj_temperatura):
    temperatura = float(input("Unesite temperaturu: "))
    if(temperatura > 0):
        broj_pozitivnih_unosa += 1
        suma_pozitivnih_temperatura += temperatura
    else:
        broj_negativnih_unosa += 1
        suma_negativnih_temperatura += temperatura

print(f"Prosjek pozitivnih temperatura je: {suma_pozitivnih_temperatura / broj_pozitivnih_unosa}")
print(f"Prosjek negativnih temperatura je: {suma_negativnih_temperatura / broj_negativnih_unosa}")