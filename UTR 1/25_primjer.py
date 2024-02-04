# Napišite program koji će učitati koliko novaca ima Marko i cijenu jedne lizalice, a zatim
# će ispisati najveći mogući broj lizalica koje Marko može kupiti te koliko će mu još ostati novaca

bankovni_balans = float(input("Molimo vas da unesete iznos novca s kojim raspolažete: "))
cijena_lizalice = float(input("Koja je cijena lizalice: "))

max_lizalica = bankovni_balans // cijena_lizalice
ostatak_novca = bankovni_balans - (max_lizalica * cijena_lizalice)

print(f"Možete kupiti {max_lizalica}.\n" + 
      f"Vaš preostao novac na računu je: {ostatak_novca}")
