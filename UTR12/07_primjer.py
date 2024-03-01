# Proširite klasu Vrijeme definirajući relacijske operacije > (veće od), < (manje od) i ==;
# (jednako). Zatim napišite program koji će omogućiti unos dva objekta tipa Vrijeme i ispisivati je
# li prvo vrijeme manje, veće ili jednako drugom vremenu.

class Vrijeme:
    def __init__(self, sati, minute):
        self.sati = sati
        self.minute = minute

    def digitalni_sat(self):
        return f"{self.sati:02d}:{self.minute:02d}"
    
    def __gt__(self, other):
        if self.sati > other.sati:
            return True
        elif self.sati == other.sati and self.minute > other.minute:
            return True
        return False

    def __lt__(self, other):
        if self.sati < other.sati:
            return True
        elif self.sati == other.sati and self.minute < other.minute:
            return True
        return False

    def __eq__(self, other):
        return self.sati == other.sati and self.minute == other.minute


sati1 = int(input("Unesite sate za prvo vrijeme: "))
minute1 = int(input("Unesite minute za prvo vrijeme: "))
vrijeme1 = Vrijeme(sati1, minute1)
                   
sati2 = int(input("Unesite sate za drugo vrijeme: "))
minute2 = int(input("Unesite minute za drugo vrijeme: "))
vrijeme2 = Vrijeme(sati2, minute2)

if vrijeme1 > vrijeme2:
    print("Prvo vrijeme je veće od drugog.")
elif vrijeme1 < vrijeme2:
    print("Prvo vrijeme je manje od drugog.")
else:
    print("Vremena su jednaka.")
