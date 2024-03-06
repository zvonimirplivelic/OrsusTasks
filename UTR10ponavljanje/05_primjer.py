# Napisati funkciju rastavi koja za zadani pozitivni četveroznamenkasti broj u pozivajući program vraća dva cijela
# broja: cijeli broj koji predstavlja prve dvije znamenke i cijeli broj koji predstavlja zadnje dvije znamenke zadanog broja.
# Napisati glavni program koji s tipkovnice učitava samo jedan cijeli broj. Ako je učitan pozitivan četveroznamenkasti broj, tada
# učitani broj rastaviti pomoću funkcije rastavi i ispisati rezultat, u suprotnom ispisati poruku: Broj nije ispravan;.

def rastavi(broj):
    if 1000 <= broj <= 9999:
        prve_dvije_znamenke = broj // 100
        zadnje_dvije_znamenke = broj % 100
        return prve_dvije_znamenke, zadnje_dvije_znamenke
    else:
        print("Broj nije ispravan.")

unos_broja = int(input("Unesite cijeli broj: "))

prve_znamenke, zadnje_znamenke = rastavi(unos_broja)

print(f"Prve dvije znamenke: {prve_znamenke}")
print(f"Zadnje dvije znamenke: {zadnje_znamenke}")
