# Napišite program koji će unositi string i iza svakog znaka 
# ispisivati znak "-" osim iza zadnjeg slova.

unos_stringa = str(input("Molim vas da unesete tekst: ")).upper()
nova_rijec = ""

for slovo in unos_stringa:
    nova_rijec += (slovo + "-")

print(nova_rijec[:-1])
