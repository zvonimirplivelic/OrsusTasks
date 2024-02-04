# Napišite program koji učitava troznamenkasti broj, 
# zatim ga ispisuje obrnutim redosljedom

broj = int(input("Unesite troznamenkasti broj: "))

prva_znamenka = broj // 100
druga_znamenka = broj // 10 % 10
treća_znamenka = broj % 10

umnožak_znamenaka = prva_znamenka * druga_znamenka * treća_znamenka 

obrnuti_broj = treća_znamenka * 100 + druga_znamenka * 10 + prva_znamenka

print(f"\nUnijeli ste broj: {broj}\n" + 
      f"Obrnuti broj je: {obrnuti_broj}")
