# Napišite program koji će kreirati prozor koji će se sastojati od dva gumba „Prenesi“ i „Izlazak“.
# Kada korisnik pritisne gumb „Prenesi“ ispisuje se „Poruka se prenosi“ u terminal. Kada korisnik
# pritisne gumb „Izlazak“ povezuje se s command=quit gdje korisnik dobiva poruku vezanu za
# izlazak iz programa.

import tkinter as tk

def prenesi_poruku():
    print("Poruka se prenosi")

def izadi_iz_programa():
    print("Izlazak iz programa...")
    root.quit()

root = tk.Tk()
root.title("tk")

button_prenesi = tk.Button(root, text="Prenesi", command=prenesi_poruku)
button_prenesi.pack(pady=10)

button_izlazak = tk.Button(root, text="Izlazak", command=izadi_iz_programa)
button_izlazak.pack(pady=10)

root.mainloop()