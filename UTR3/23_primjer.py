# Napišite program koji će učitati brojeve sve dok su dijeljivi s 5 te kasnije ispisuje
# aritmetičku sredinu učitanih brojeva koji su veći od 50 i manji od 100

suma_brojeva = 0
i = 0

while True:
    unos_broja = int(input("Molim vas da unesete broj: "))
    if unos_broja %5 != 0:
        break

    if unos_broja in range(50, 100):
        i = i + 1 
        suma_brojeva += unos_broja

print(f"Aritmetička sredina unešenih brojeva u rasponu od 50 do 100 iznosi: {suma_brojeva / i}")