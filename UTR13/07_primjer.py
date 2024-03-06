# Napišite program koji će kreirati prozor u čijoj će labeli pisati poruka: „Ucimo Python“ koristeći
# Tkinter mode.

import tkinter as tk

root = tk.Tk()
root.title("Ucimo Python")

label = tk.Label(root, text="Ucimo Python")
label.pack(padx=20, pady=20)

root.mainloop()