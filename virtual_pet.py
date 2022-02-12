"""
    рисунки питомца,
    способности питомца,
    показатели питомца,
    время
"""

import tkinter as tk
#form pet import Pet
from PIL import Image, ImageTk

class App(tk.Tk):
    def __init__(self):
        super().__init__()


if __name__== '__main__':
    window = App()
    window.mainloop()

canvas = tkinter.Canvas(root, height=400, width=700)
image = Image.open("happy.png")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw',image=photo)
canvas.grid(row=2,column=1)
root.mainloop()