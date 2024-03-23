# Napišite program koji će kreirati prozor u čijoj će labeli pisati poruka: „Ucimo Python“ koristeći
# Tkinter mode.

import tkinter as tk

root = tk.Tk()
root.title("Učimo Python")

label = tk.Label(root, text="Učimo Python")
label.pack(padx=32, pady=32)  # Postavljanje razmaka oko natpisa

root.mainloop()

