from tkinter import *
from config import Config
import random

class Apple(Frame):
    def __init__(self, master):
        super().__init__(master=master, background="red", width=25, height=25)
        self.grid(row=random.randint(0, Config.GRID_ROWS - 1), column=random.randint(0, Config.GRID_COLUMNS - 1))
