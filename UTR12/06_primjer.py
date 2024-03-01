# Napišite program koji definira klasu Vrijeme, koja će sadržavati svojstva za sate i minute. Proširite
# klasu Vrijeme dodajući metodu repr(self) koja će omogućiti ispis vremena na digitalnom satu u
# formatu HH:MM;. Zatim napišite program koji će omogućiti unos sati i minuta, te koristeći ovu
# klasu, ispisati vrijeme u formatu HH:MM.

class Vrijeme:
    def __init__(self, sati, minute):
        self.sati = sati
        self.minute = minute

    def repr(self):
        return f"{self.sati:02d}:{self.minute:02d}"

while True:
    try:
        sati = int(input("Unesite sate: "))
        if not (0 <= sati <= 23):
            raise ValueError("Sati trebaju biti u rasponu od 0 do 23.")

        minute = int(input("Unesite minute: "))
        if not (0 <= minute <= 59):
            raise ValueError("Minute trebaju biti u rasponu od 0 do 59.")

        vrijeme = Vrijeme(sati, minute)
        # Ispis rezultata
        print(f"Vrijeme na satu: {vrijeme.repr()}")
        
        break
    except ValueError as e:
        print(f"Greška: {e}")
        print("Molimo unesite ispravne vrijednosti za sate i minute.")