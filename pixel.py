from tkinter import *
class Pixel(Frame):
    def __init__(self, parent, x, y):
        super().__init__(parent, width=16, height=16, bg="blue")
        self.place(x=x*16, y=y*16)