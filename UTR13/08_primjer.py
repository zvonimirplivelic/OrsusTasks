# Napišite program koji će kreirati prozor u čijoj će labeli pisati poruka u tri reda: „Python je super
# programski jezik. Jednostavan je i sintaksa nije komplicirana. U drugim programskim jezicima bilo
# bi puno teže“. Potrebno je ubaciti sliku Python loga.

import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Python je super")

#image_path = "python.jpg"
#image = Image.open(image_path)
#image = image.resize(250, 250)
#photo = ImageTk.PhotoImage(image)

label = tk.Label(root, text="Python je super\nprogramski jezik.\nJednostavan je i sintaksa nije komplicirana.")
label.pack(padx=20, pady=20)

#image_label = tk.Label(root, image=photo)
#image_label.image = photo  

root.mainloop()