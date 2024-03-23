# Napišite program koji koristi Entry Widgets te omogućuje unos teksta Ime i Prezime. Koristite grid
# za pozicioniranje polja za unos teksta.

import tkinter as tk

def prikazi_podatke():
    ime = unos_ime.get()
    prezime = unos_prezime.get()
    print("Ime:", ime)
    print("Prezime:", prezime)

root = tk.Tk()
root.title("Unos Imena i Prezimena")

tk.Label(root, text="Ime:").grid(row=0, column=0)
unos_ime = tk.Entry(root)
unos_ime.grid(row=0, column=1)

tk.Label(root, text="Prezime:").grid(row=1, column=0)
unos_prezime = tk.Entry(root)
unos_prezime.grid(row=1, column=1)

tk.Button(root, text="Prikazi", command=prikazi_podatke).grid(row=2, columnspan=2, pady=10)

root.mainloop()