# Napišite program koji učitava tri broja te ispisuje
# redosljedom najmanji, srednji i najveći broj

broj_a = input("Molim vas da unesete broj: ")
broj_b = input("Molim vas da unesete broj: ")
broj_c = input("Molim vas da unesete broj: ")

if broj_a > broj_b:
    broj_a, broj_b = broj_b, broj_a
if broj_a > broj_c:
    broj_a, broj_c = broj_c, broj_a
if broj_b > broj_c:
    broj_b, broj_c = broj_c, broj_b

print (f"{broj_a} < {broj_b} < {broj_c}")

    