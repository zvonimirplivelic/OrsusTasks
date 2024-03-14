# Napišite program koji će kreirati prozor u čijoj će labeli pisati poruka u tri reda: „Python je super
# programski jezik. Jednostavan je i sintaksa nije komplicirana. U drugim programskim jezicima bilo
# bi puno teže“. Potrebno je ubaciti sliku Python loga.

import tkinter as tk
from PIL import Image, ImageTk

message = "Python je super programski jezik.\nJednostavan je i sintaksa nije komplicirana.\nU drugim programskim jezicima bilo bi puno teže."

root = tk.Tk()
root.title("Python je super")

image = Image.open("UTR13\img\python.jpg")
image.resize = (250, 250)
photo = ImageTk.PhotoImage(image)

label = tk.Label(root, text= message, justify = tk.LEFT)
label.grid(row = 0, column = 0, padx = 20, pady = 20)

image_label = tk.Label(root, image=photo)
image_label.image = photo  
image_label.grid(row = 0, column = 1, padx = 20, pady = 20)

root.mainloop()