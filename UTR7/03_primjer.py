# Napišite program koji učitava tri broja koja predstavljaju trenutno vrijeme u satima, minutama i
# sekundama te pohranjuje vrijednosti u tuple. Potrebno je ispisati točno trenutno vrijeme i
# vrijeme na digitalnom satu koji pokazuje samo sat i minute.

sati = int(input("Unesite sate: "))
minute = int(input("Unesite minute: "))
sekunde = int(input("Unesite sekunde: "))

vrijeme = (sati, minute, sekunde)

print("Unešeno vrijeme:", vrijeme)

print("Vrijeme na digitalnom satu:", (vrijeme[0], vrijeme[1]))