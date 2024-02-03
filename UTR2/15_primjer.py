# Napišite program koji učitava broj pogodata tima A i tima B,
# zatim ispisuje odgovarajuću poruku "Tim A je pobjedio.";
# ili "Tim B je pobjedio."; ili "bez pobjednika"

broj_pogodaka_tim_a = int(input("Unesite broj pogodaka tima A: "))
broj_pogodaka_tim_b = int(input("Unesite broj pogodaka tima B: "))

if(broj_pogodaka_tim_a > broj_pogodaka_tim_b):
    print("Tim A je pobjedio")
elif(broj_pogodaka_tim_a < broj_pogodaka_tim_b):
    print("Tim B je pobjedio")
else:
    print("Nema pobjednika")
