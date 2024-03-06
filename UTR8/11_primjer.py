# [BONUS] Napiši program koji će unositi string te ispisuje koliko djelitelja ima zbroj ASCII
# vrijednosti svih znakova u stringu. Napišite funkciju ascii_sumator koja za ulazni parametar koji
# je broj vraća broj njegovih djelitelja.

def ascii_sumator(broj):
    broj_djelitelja = 0

    for i in range(1, broj + 1):
        if broj % i == 0:
            broj_djelitelja += 1

    return broj_djelitelja

unos_stringa = input("Unesite string: ")

zbroj_ascii = sum(ord(znak) for znak in unos_stringa)

broj_djelitelja = ascii_sumator(zbroj_ascii)

print(f"Zbroj ASCII vrijednosti znakova u stringu: {zbroj_ascii}")
print(f"Broj djelitelja zbroja ASCII vrijednosti: {broj_djelitelja}")