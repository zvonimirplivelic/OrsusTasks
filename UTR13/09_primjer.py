# Napišite program koji će kreirati prozor koji će se sastojati od tri labele. Opis fonta, veličine i
# ostalog je dan u samom tekstu na slici.

import tkinter as tk

root = tk.Tk()
root.title("tk")

prva_poruka = "Crveni tekst u Times fontu"
druga_poruka = "Bijeli tekst u Helvetica 16 bold italic fontu."
treca_poruka = "Plavi tekst u žutoj pozadini Verdana fontu"

label1 = tk.Label(root, text = prva_poruka, fg = "red", font = ("Times", 12))
label1.grid(row=0, column=0)

label2 = tk.Label(root, text = druga_poruka, fg = "white", bg = "green", font = ("Helvetica", 16, "bold italic"))
label2.grid(row=1, column=0)

label3 = tk.Label(root, text = treca_poruka, fg = "blue", bg = "yellow", font = ("Verdana", 12))
label3.grid(row=2, column=0)

root.mainloop()