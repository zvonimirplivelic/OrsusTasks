# Napišite program koji učitava pet brojeva te ispisuje najmanji i najveći broj.

lista_brojeva = []

for i in range (0, 5):
    unos_broja = int(input("Molim vas unesite broj: "))
    lista_brojeva.append(unos_broja)

najmanji_broj = min(lista_brojeva)
najveći_broj = max(lista_brojeva)

print(f"Najmanji element liste: {najmanji_broj}\n" +
      f"Najveći broj liste: {najveći_broj}")