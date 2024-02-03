# Napišite program koji će učitati cijenu i popust kožne lopte, zatim ispisuje konačnu cijenu s popustom

cijenaKožneLopte = float(input("Molim vas da unesete cijenu kožne lopte: "))
popust = float(input("Molim vas da unesete postotak popusta na artikl: "))

cijenaSaPopustom = cijenaKožneLopte - (cijenaKožneLopte * (1 / popust))

print(f"Cijena kožne lopte je {cijenaKožneLopte}€. Korigirana cijena sa popustom od {popust}% je {cijenaSaPopustom}€")