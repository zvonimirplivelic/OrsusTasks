# Napišite program koji učitava 5 kuglica u Jackpot igri.
# Pretpostavite da su mogući samo brojevi od 1 do 50.
# Nakon toga potrebno je ispisati Joker broj. Joker broj
# predstavlja znamenku na mjestu jedinice.
# UPUTA: Ako je korisnik upisao 7,23,9,44,50 tada je Joker broj 73940

prva_kuglica = int(input("Prva kuglica: "))
druga_kuglica = int(input("Druga kuglica: "))
treća_kuglica = int(input("Treća kuglica: "))
četvrta_kuglica = int(input("Četvrta kuglica: "))
peta_kuglica = int(input("Peta kuglica: "))

print(f"{prva_kuglica % 10}{druga_kuglica % 10}{treća_kuglica % 10}{četvrta_kuglica % 10}{peta_kuglica % 10}")