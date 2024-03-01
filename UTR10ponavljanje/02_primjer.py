# Napisati funkciju zamijeni koja prolazi kroz niz i zamjenjuje svaku
# pojavu traženog znaka sa znakom ?. Napisati program koji će
# učitati niz znakova, provjeriti da je najviše 20 znakova učitano.
# Nakon toga u slijedećem retku učitati znak koji je potrebno
# zamijeniti s upitnikom ?. Potrebno je ispisati novi niz s
# upitnikom.

def zamijeni(niz, traženi_znak):
    return ''.join(['?' if znak == traženi_znak else znak for znak in niz])

niz = input("Unesite niz znakova (najviše 20 znakova): ")[:20]

traženi_znak = input("Unesite znak koji želite zamijeniti s '?': ")

if len(traženi_znak) == 1:
    novi_niz = zamijeni(niz, traženi_znak)
    print(f"Novi niz s upitnicima: {novi_niz}")
else:
    print("Unesite samo jedan znak za zamjenu.")
