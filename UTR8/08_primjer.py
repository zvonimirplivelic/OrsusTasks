# Napišite program koji će unositi listu brojeva te funkciju zbroji 
# koja će zbrojiti sve elemente u listi.

def zbroji(lista):
    zbroj = sum(lista)
    return zbroj

lista_brojeva = []

while True:
    unos_broja = int(input("Unesite broj (0 za prekid): "))

    if(unos_broja == 0):
        break
    
    lista_brojeva.append(unos_broja)


print(f"Zbroj svih brojeva u listi je: {zbroji(lista_brojeva)}") 