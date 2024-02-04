# Napišite program koji učitava dva troznamenkasta broja, zatim ispisuje
# zbroj prvog unesenog broja i drugog broja upisanog obrnutim redosljedom.
# UPUTA: 123 + 456 -> 123 + 654 = 777

prvi_broj = int(input("Unesite prvi troznamenkasti broj: "))
drugi_broj = int(input("Unesite drugi troznamenkasti broj: "))

prva_znamenka = drugi_broj // 100
druga_znamenka = drugi_broj // 10 % 10
treća_znamenka = drugi_broj % 10

obrnuti_drugi_broj = treća_znamenka * 100 + druga_znamenka * 10 + prva_znamenka

zbroj_brojeva = prvi_broj + obrnuti_drugi_broj

print(f"\nUnijeli ste brojeve: {prvi_broj} i {drugi_broj}\n" + 
      f"Obrnuti drugi broj je: {obrnuti_drugi_broj}\n" +
      f"Zbroj brojeva je: {zbroj_brojeva}")
