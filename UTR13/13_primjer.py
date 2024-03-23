# Napišite program koji će koristeći Radio gumbe pitati korisnika za spol: muški ili ženski. Nakon
# toga je potrebno dodati gumb „Potvrdi“ koji je povezan sa showinfo i omogućuje otvaranje
# skoknog prozora gdje se prikaže poruka: „Odabrali ste:“

import tkinter as tk
from tkinter import messagebox

def prikazi_poruku():
    spol = var_spol.get()
    if spol == 1:
        messagebox.showinfo("Odabir spola", "Odabrali ste: Muški")
    elif spol == 2:
        messagebox.showinfo("Odabir spola", "Odabrali ste: Ženski")

root = tk.Tk()
root.title("Odabir spola")

var_spol = tk.IntVar()

label = tk.Label(root, text = "Odaberi spol:")
label.pack()
tk.Radiobutton(root, text="Muški", variable=var_spol, value=1).pack()
tk.Radiobutton(root, text="Ženski", variable=var_spol, value=2).pack()

tk.Button(root, text="Potvrdi", command=prikazi_poruku).pack()

root.mainloop()
