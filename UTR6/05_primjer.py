# Napišite program koji će učitavati prvo popis ispravno napisanih engleskih riječi odvojene zarezom.
# Nakon toga u novi red učitava se popis riječi koje je napisao polaznik. Program treba ispisati koliko
# riječi je polaznik pogrešno napisao. Potrebno je riješiti zadatak koristeći skupove.

ispravne_rijeci = input("Unesite popis ispravnih riječi odvojenih zarezom: ")
polaznikove_rijeci = input("Unesite popis polaznikovih riječi odvojenih zarezom: ")

ispravne_set = set(ispravne_rijeci.upper().split(','))
polaznikove_set = set(polaznikove_rijeci.upper().split(','))

pogresno_napisane = polaznikove_set - ispravne_set

print(f"Broj pogrešno napisanih riječi: {len(pogresno_napisane)}")