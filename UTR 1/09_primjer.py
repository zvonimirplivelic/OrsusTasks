# Napišite program koji učitava dva prirodna broja, zatim ispisuje njihov zbroj, razliku, umnožak, kvocijent i ostatak pri dijeljenju

prviBroj = int(input("Molim vas da unesete prvi broj: "))
drugiBroj = int(input("Molim vas da unesete drugi broj: "))

zbrojBrojeva = prviBroj + drugiBroj
razlikaBrojeva = prviBroj - drugiBroj
umnožakBrojeva = prviBroj * drugiBroj
kvocijentBrojeva = prviBroj / drugiBroj
ostatakPriDijeljenju = prviBroj % drugiBroj

print(f"Zbroj brojeva je {zbrojBrojeva}")
print(f"Razlika brojeva je {razlikaBrojeva}")
print(f"Umnožak brojeva je {umnožakBrojeva}")
print(f"Kvocijent brojeva je {kvocijentBrojeva}")
print(f"Osttak pri dijeljenju brojeva je {ostatakPriDijeljenju}")
