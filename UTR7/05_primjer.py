# Napišite program koji učitava predefiniranu listu tri ntorki. Zatim se učita godina te je potrebno
# ispisati sve osobe koje su rođene nakon učitane godine.

osobe = [
    ("Marko", 1988),
    ("Marija", 1991),
    ("Ivan", 1986)
]

unesena_godina = int(input("Unesite godinu: "))

mlade_osobe = [(ime, godina) for ime, godina in osobe if godina > unesena_godina]

print(f"Osobe rođene nakon {unesena_godina} godine:")
for osoba in mlade_osobe:
    print(f"{osoba[0]} {osoba[1]}")