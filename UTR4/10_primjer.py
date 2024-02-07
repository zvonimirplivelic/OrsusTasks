# Napišite program koji će unositi string u kojem sva velika slova promijeni u mala, 
# a iz stringa uz to uklanja sve točke i zareze. 

unos_stringa = input("Molim vas da unesete tekst: ")

unos_stringa = unos_stringa.replace(".", "").replace(",", "").lower()

print(unos_stringa)