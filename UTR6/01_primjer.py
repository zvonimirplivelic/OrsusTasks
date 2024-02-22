# Napišite program koji će unositi dvije riječi i ispisivati ukupni broj različitih znakova
# koji se nalaze u tim riječima. Potrebno je riješiti zadatak koristeći skupove.

prvi_set = set(input("Unesi prvu riječ: "))
drugi_set = set(input("Unesi drugu riječ: "))

ukupno_slova = prvi_set & drugi_set

print(f"Ukupni broj istih znakova koji se nalaze u tim riječima: {len(ukupno_slova)}\n" +
      f"Slova koja su zajednička su: {ukupno_slova}")