# Napišite program koji će unositi prirodan broj n koji predstavlja broj gradova. Nakon toga potrebno
# je u svaki redak unijeti ime grada, a zatim 12 prirodnih brojeva koji predstavljaju prosječnu
# temperaturu za određeni mjesec (odvojene samo razmakom). Program treba ispisati nazive
# gradova sortirane po srednjoj godišnjoj temperaturi (silazno), po jedan grad u svaki redak. Potrebno
# je riješiti zadatak koristeći rječnik.

# Napišite program koji će unositi prirodan broj n koji predstavlja broj gradova. Nakon toga potrebno
# je u svaki redak unijeti ime grada, a zatim 12 prirodnih brojeva koji predstavljaju prosječnu
# temperaturu za određeni mjesec (odvojene samo razmakom). Program treba ispisati za svaki grad
# naziv grada te prosječnu godišnju temperaturu. Potrebno je riješiti zadatak koristeći rječnik.


n = int(input("Unesite broj gradova: "))

gradovi = {}

for i in range(n):
    ime_grada = input("Unesite ime grada: ")
    temperature = list(map(int, input("Unesite prosječne temperature za svaki mjesec (razdvojene razmakom): ").split()))
    
    srednja_godisnja_temperatura = sum(temperature) / len(temperature)
    
    gradovi[ime_grada] = {
        'srednja_godisnja_temperatura': srednja_godisnja_temperatura,
        'temperature_po_mjesecima': temperature
    }

sortirani_gradovi = sorted(gradovi.items(), key=lambda x: x[1]['srednja_godisnja_temperatura'], reverse=True)

print("Gradovi sortirani po srednjoj godišnjoj temperaturi (silazno):")

for grad, podaci in sortirani_gradovi:
    print(f"{grad}:\t Temp po mjesecu{podaci['temperature_po_mjesecima']};\tSredišnja temp: {podaci['srednja_godisnja_temperatura']}")