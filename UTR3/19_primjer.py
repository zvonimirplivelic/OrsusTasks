# Napišite program koji će unositi brojeve sve dok ne unese broj 0,
# zatim ispisuje samo dvoznamenkaste brojeve

while True:
    unos_broja = int(input("Molimo vas da unesete broj:"))
    if(unos_broja == 0):
        break
    if(unos_broja >= 10):
        print(unos_broja)