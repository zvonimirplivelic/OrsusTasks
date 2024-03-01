# Potrebno je definirati klasu Film. Svaki film ima atribute: naslov, redatelj, godina izdanja i trajanje
# u minutama. Implementirajte konstruktor koji prima te atribute i inicijalizira ih. Nakon toga,
# dodajte metodu &quot;informacije&quot; koja ispisuje osnovne informacije o filmu (naslov, redatelj, godina
# izdanja). Nakon definiranja klase za film, potrebno je definirati klasu Videoteka. Svaka videoteka ima
# atribute: naziv videoteke i listu filmova. Implementirajte konstruktor koji prima naziv videoteka i
# inicijalizira praznu listu filmova. Dodajte metodu &quot;dodaj_film&quot; koja dodaje novi film u listu
# filmova videoteku. Također, dodajte metodu &quot;pretrazi_filmove&quot; koja prima naslov filma i ispisuje
# informacije o tom filmu ako se nalazi u videoteci, inače ispisuje poruku &quot;Film nije pronađen.&quot;
# Nakon definiranja klase videoteka i metoda za dodavanje i pretraživanje filmova, možete kreirati
# nekoliko filmova s različitim naslovima, redateljima, godinama izdanja i trajanjem. Zatim stvorite
# videoteku i dodajte filmove u nju. Na kraju je potrebno ispisati informacije o filmovima u
# videotheci i pretražiti filmove po naslovu.

class Film:
    def __init__(self, naslov, redatelj, godina_izdanja, trajanje):
        self.naslov = naslov
        self.redatelj = redatelj
        self.godina_izdanja = godina_izdanja
        self.trajanje = trajanje

    def informacije(self):
        print(f"Film: {self.naslov}\nRedatelj: {self.redatelj}\nGodina izdanja: {self.godina_izdanja}\nTrajanje: {self.trajanje} min")

class Videoteka:
    def __init__(self, naziv):
        self.naziv = naziv
        self.filmovi = []

    def dodaj_film(self, film):
        self.filmovi.append(film)
        print(f"Film '{film.naslov}' dodan u videoteku.")

    def pretrazi_filmove(self, naslov):
        for film in self.filmovi:
            if film.naslov == naslov:
                film.informacije()
                return
        print(f"Film '{naslov}' nije pronađen u videoteci.")

film1 = Film("Matrix", "Redatelj 1", 2020, 120)
film2 = Film("Fight Club", "Redatelj 2", 2018, 95)
film3 = Film("Ace Ventura", "Redatelj 3", 2015, 110)

videoteka = Videoteka("Videoteka")

videoteka.dodaj_film(film1)
videoteka.dodaj_film(film2)
videoteka.dodaj_film(film3)

print("\nInformacije o filmovima u videoteci:")
for film in videoteka.filmovi:
    film.informacije()

print("\nPretraživanje filmova po naslovu:")
videoteka.pretrazi_filmove("Film 1")
videoteka.pretrazi_filmove("Nepostojeći film")
