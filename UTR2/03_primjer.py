# Napišite program koji učitava dva decimalna broja, zatim ispisuje izračunava
# njihov zbroj, razliku, umnožak, kvocijent i ostatak pri dijeljenju

prviBroj = float(input("Unesite prvi decimalni broj: "))
drugiBroj = float(input("Unesite drugi decimalni broj: "))

zbroj = prviBroj + drugiBroj
razlika = prviBroj - drugiBroj
umnožak = prviBroj * drugiBroj
kvocijent = prviBroj / drugiBroj
modulo = prviBroj % drugiBroj

print(f"\nZbroj brojeva je: {zbroj}\n"+ 
      f"Razlika brojeva je: {razlika}\n" +
      f"Umnožak brojeva je: {umnožak}\n" +
      f"Kvocijent brojeva je: {kvocijent}\n" + 
      f"Ostatak pri dijeljenju brojeva je: {modulo}\n")
