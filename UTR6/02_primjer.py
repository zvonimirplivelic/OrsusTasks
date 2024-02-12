# Napišite program koji će unositi dvije riječi i ispisivati ukupni broj istih 
# znakova koji se nalaze u tim riječima. Zadatak je potrebno riješiti koristeći skupove

prvi_set = set(input("Unesi prvu riječ: "))
drugi_set = set(input("Unesi drugu riječ: "))

ukupno_slova = prvi_set & drugi_set

print(f"Ista slova u setovima: {ukupno_slova}")