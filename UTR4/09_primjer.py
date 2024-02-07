# Napišite program koji će unositi string i ispisuje broj pojavljivanja 
# riječi u navedenom stringu. Pretpostavite da su riječi unutar rečenice odvojene razmakom.

unos_stringa = str(input("Molim vas da unesete tekst: "))

broj_rijeci = len(unos_stringa.split())

print(f"Broj riječi: {broj_rijeci}")