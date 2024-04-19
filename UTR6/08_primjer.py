# Napišite program koji će učitati string i nakon toga odrediti sve diftonge i ispisati ih sortirane po
# broju pojavljivanja silazno. Diftonzi čine dva susjedna slova. Potrebno je riješiti zadatak koristeći
# rječnik.

string = input("Unesite string: ")
brojac_diftonga = {}

for i in range(len(string) - 1):
    diftong = string[i:i+2]
    
    if diftong.isalpha() and len(diftong) == 2:
        brojac_diftonga[diftong] = brojac_diftonga.get(diftong, 0) + 1

sortirani_diftonzi = sorted(brojac_diftonga.items(), key=lambda x: x[1], reverse=True)


print("Diftonzi sortirani po broju pojavljivanja:")
for diftong, broj_pojavljivanja in sortirani_diftonzi:
    print(f"{diftong}: {broj_pojavljivanja}")