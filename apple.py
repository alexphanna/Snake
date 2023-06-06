from tkinter import *
from config import config
import random

class Apple(Frame):
    def __init__(self, master):
        super().__init__(master=master, background="red", width=config["pixel_size"], height=config["pixel_size"])
        self.grid(row=random.randint(0, config["grid_rows"] - 1), column=random.randint(0, config["grid_columns"] - 1))
