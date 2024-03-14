# Napišite program koji će koristeći Radio gumbe pitati korisnika za spol: muški ili ženski.

import tkinter as tk

def prikazi_odabir():
    spol = var_spol.get()
    if spol == 1:
        print("Odabrali ste muški spol.")
    elif spol == 2:
        print("Odabrali ste ženski spol.")

root = tk.Tk()
root.title("Odabir spola")
var_spol = tk.IntVar()

label = tk.Label(root, text = "Odaberi spol:")
label.pack()
tk.Radiobutton(root, text="Muški", variable=var_spol, value=1).pack()
tk.Radiobutton(root, text="Ženski", variable=var_spol, value=2).pack()

tk.Button(root, text="Potvrdi", command=prikazi_odabir).pack()

root.mainloop()