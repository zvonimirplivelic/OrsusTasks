# Proširite klasu Vrijeme definirajući operaciju zbrajanja koja će omogućiti dodavanje n minuta
# postojećem vremenu. Zatim napišite program koji će omogućiti unos sata, minuta i još jednog
# cijelog broja n (vrijeme u minutama), te ispisati konačno vrijeme dobiveno dodavanjem n minuta
# originalnom vremenu.

class Vrijeme:
    def __init__(self, sati, minute):
        self.sati = sati
        self.minute = minute

    def pokazi_vrijeme(self):
        return f"{self.sati:02d}:{self.minute:02d}"

    def __add__(self, n):
        sati = self.sati + (self.minute + n) // 60
        minute = (self.minute + n) % 60

        return Vrijeme(sati, minute)

sati = int(input("Unesite sate: "))
minute = int(input("Unesite minute: "))
vrijeme = Vrijeme(sati, minute)

n = int(input("Unesite broj minuta koje želite dodati: "))

novo_vrijeme = vrijeme + n

print(f"Originalno vrijeme: {vrijeme.pokazi_vrijeme()}")
print(f"Novo vrijeme nakon dodavanja {n} minuta: {novo_vrijeme.pokazi_vrijeme()}")