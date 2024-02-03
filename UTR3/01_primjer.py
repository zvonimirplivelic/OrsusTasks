# Napiši program koji učitava dva broja te svaki puta oduzima od većeg broja manji

prvi_broj = int(input("Unesite prvi broj: "))
drugi_broj = int(input("Unesite drugi broj: "))

if prvi_broj < drugi_broj:
    rezultat = drugi_broj - prvi_broj
else: rezultat = prvi_broj - drugi_broj

print(f"Rezultat: {rezultat}")