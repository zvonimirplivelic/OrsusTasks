# Napišite program koji će unositi string te ispisati novi string 
# tako da se treće slovo zamijeni ljestvama i na kraju niza potrebno je dodati znak 007. 

unos_stringa = input("Molim vas da unesete tekst: ")

print(unos_stringa.replace(unos_stringa[2], "#") + "007")