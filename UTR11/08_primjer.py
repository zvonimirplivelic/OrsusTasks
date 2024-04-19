# Napišite program koji će iz ulazne datoteke ulaz.txt unositi imena i prezimena osoba (kao jedan
# string) te u datoteku u odgovarajući redak ispisivati inicijale (prvo slovo imena i prvo slovo
# prezimena, iza kojih se nalazi znak .

with open('ulaz.txt', 'r') as ulazna_datoteka, open('izlaz.txt', 'w') as izlazna_datoteka:
    for linija in ulazna_datoteka:
        ime_i_prezime = linija.strip().split()
        if len(ime_i_prezime) >= 2:
            inicijali = ime_i_prezime[0][0].upper() + '.' + ime_i_prezime[1][0].upper() + '.'
            izlazna_datoteka.write(inicijali + '\n')