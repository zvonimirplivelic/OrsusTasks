# Napišite program koji će unositi prirodan broj n koji predstavlja broj gradova. Nakon toga potrebno
# je u svaki redak unijeti ime grada, a zatim 12 prirodnih brojeva koji predstavljaju prosječnu
# temperaturu za određeni mjesec (odvojene samo razmakom). Program treba ispisati nazive
# gradova sortirane po srednjoj godišnjoj temperaturi (silazno), po jedan grad u svaki redak. Potrebno
# je riješiti zadatak koristeći rječnik.

# Napišite program koji će unositi prirodan broj n koji predstavlja broj gradova. Nakon toga potrebno
# je u svaki redak unijeti ime grada, a zatim 12 prirodnih brojeva koji predstavljaju prosječnu
# temperaturu za određeni mjesec (odvojene samo razmakom). Program treba ispisati za svaki grad
# naziv grada te prosječnu godišnju temperaturu. Potrebno je riješiti zadatak koristeći rječnik.


# Unos broja gradova
n = int(input("Unesite broj gradova: "))

# Rječnik za pohranu podataka o gradovima
gradovi = {}

# Unos podataka o gradovima
for i in range(n):
    ime_grada = input("Unesite ime grada: ")
    temperature = list(map(int, input("Unesite prosječne temperature za svaki mjesec (razdvojene razmakom): ").split()))
    
    # Računanje srednje godišnje temperature
    srednja_godisnja_temperatura = sum(temperature) / len(temperature)
    
    # Dodavanje podataka u rječnik
    gradovi[ime_grada] = {
        'srednja_godisnja_temperatura': srednja_godisnja_temperatura,
        'temperature_po_mjesecima': temperature
    }

# Sortiranje gradova po srednjoj godišnjoj temperaturi (silazno)
sortirani_gradovi = sorted(gradovi.items(), key=lambda x: x[1]['srednja_godisnja_temperatura'], reverse=True)

# Ispis rezultata
print("Gradovi sortirani po srednjoj godišnjoj temperaturi (silazno):")
for grad, podaci in sortirani_gradovi:
    print(f"{grad}:\t Temp po mjesecu{podaci['temperature_po_mjesecima']};\tSredišnja temp: {podaci['srednja_godisnja_temperatura']}")