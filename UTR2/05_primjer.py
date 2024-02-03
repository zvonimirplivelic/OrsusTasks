# Napišite program koji učitava peteroznamenkasti broj, 
# zatim ispisuje sumu znamenaka učitanog broja

broj = int(input("Unesite peteroznamenkasti broj: "))

prva_znamenka = broj // 10000
druga_znamenka = (broj // 1000) % 10
treća_znamenka = (broj // 100) % 10
četvrta_znamenka = (broj // 10) % 10
peta_znamenka = broj % 10

zbroj_znamenaka = prva_znamenka + druga_znamenka + treća_znamenka + četvrta_znamenka + peta_znamenka

print(f"\nUnijeli ste broj: {broj}\n" +
      f"Prva znamenka: {prva_znamenka}\n" + 
      f"Druga znamenka: {druga_znamenka}\n" +
      f"Treća znamenka: {treća_znamenka}\n" +
      f"Četvrta znamenka: {četvrta_znamenka}\n" + 
      f"Peta znamenka: {peta_znamenka}\n" +
      f"Zbroj znamenaka: {zbroj_znamenaka}\n"
)
