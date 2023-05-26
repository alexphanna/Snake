from tkinter import *
from pixel import Pixel
class Snake():
    def __init__(self, parent):
        self.pixels = [Pixel(parent, 1, 1), Pixel(parent, 2, 1)]
    def moveUp(self):
        for pixel in self.pixels: 
            pixel.place(y=pixel.winfo_y() - 16)
    def moveLeft(self):
        for pixel in self.pixels: 
            pixel.place(x=pixel.winfo_x() - 16)
    def moveDown(self):
        for pixel in self.pixels: 
            pixel.place(y=pixel.winfo_y() + 16)
    def moveRight(self):
        for pixel in self.pixels: 
            pixel.place(x=pixel.winfo_x() + 16)