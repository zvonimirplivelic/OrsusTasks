# Napišite program koji učitava listu brojevi=[17,8,20,24,8,17] i 
# ispisuje prvi element liste, najmanji element i sumu svih elemenata.

lista_brojeva = [17, 8, 20, 24, 8, 17]

prvi_element = lista_brojeva[0]
najmanji_element = min(lista_brojeva)
suma_elemenata = sum(lista_brojeva)

print(f"Prvi element liste: {prvi_element}\n" +
      f"Najmanji element liste: {najmanji_element}\n" +
      f"Suma svih elemenata liste: {suma_elemenata}\n")