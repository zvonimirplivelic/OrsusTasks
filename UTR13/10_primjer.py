# Napišite program koji će kreirati prozor koji će se sastojati od Message widgeta gdje je za
# prelazak u novi red potrebno koristiti \n te postaviti pozadinsku boju lightgreen, font Times,
# veličine 15, bold, italic. Širina Message widgeta mora biti 400.

import tkinter as tk

root = tk.Tk()
root.title("Message Widget")
root.configure(bg = "lightgreen")

message_text = "Prelazak u novi red\n i sada smo u novom redu"
message = tk.Message(root, text=message_text, bg = "lightgreen", width=400, font=("Times", 15, "bold italic"))
message.pack(padx=0, pady=0)

root.mainloop()