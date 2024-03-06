# Napišite program koji će kreirati prozor u čijoj će labeli pisati poruka u tri reda: „Python je super
# programski jezik. Jednostavan je i sintaksa nije komplicirana. U drugim programskim jezicima bilo
# bi puno teže“. Potrebno je ubaciti sliku Python loga.

import tkinter as tk

root = tk.Tk()
root.title("Zadatak 8")

message_text = f"Python je super programski jezik.\nJednostavan je i sintaksa nije komplicirana.\nU drugim programskim jezicima bilo bi puno teže"

root.label = tk.Label(root, text=message_text)

root.mainloop()