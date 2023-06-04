from tkinter import *
from config import Config
import random

class Apple(Frame):
    def __init__(self, master):
        super().__init__(master=master, background="red", width=Config.PIXEL_SIZE, height=Config.PIXEL_SIZE)
        self.grid(row=random.randint(0, Config.GRID_ROWS - 1), column=random.randint(0, Config.GRID_COLUMNS - 1))
