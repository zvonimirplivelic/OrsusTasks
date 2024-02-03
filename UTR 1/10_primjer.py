# Napišite program koji učitava tri ocijene, zatim ispisuje prosjek

prvaOcjena = int(input("Unesite prvu ocjenu: "))
drugaOcjena = int(input("Unesite drugu ocjenu: "))
trecaOcjena = int(input("Unesite trecu ocjenu: "))

prosjekOcjena = (prvaOcjena + drugaOcjena + trecaOcjena) / 3

print(f"Prosjek ocjena je: {prosjekOcjena}")