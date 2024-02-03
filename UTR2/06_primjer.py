# Napišite program koji učitava troznamenkasti broj, 
# zatim ispisuje umnožak znamenaka učitanog broja

broj = int(input("Unesite troznamenkasti broj: "))

prva_znamenka = (broj // 100) % 10
druga_znamenka = (broj // 10) % 10
treća_znamenka = broj % 10

umnožak_znamenaka = prva_znamenka * druga_znamenka * treća_znamenka 

print(f"\nUnijeli ste broj: {broj}\n" +
      f"Prva znamenka: {prva_znamenka}\n" + 
      f"Druga znamenka: {druga_znamenka}\n" +
      f"Treća znamenka: {treća_znamenka}\n" +
      f"Zbroj znamenaka: {umnožak_znamenaka}\n"
)
