from tkinter import *
from apple import Apple
from direction import Direction

class Snake(list):
    def __init__(self, master):
        self.direction = Direction.DOWN
        self.speed = 500
        self.master = master
        self.grow(master)
    def grow(self, master):
        self.append(Frame(master=master, background="lime", width=25, height=25))
    def set_direction(self, direction):
        self.direction = direction
    def move(self):
        # moves the snake in the current direction

        if self.direction == Direction.UP:
            self.place(y=self.winfo_y()-25)
        elif self.direction == Direction.DOWN:
            self.place(y=self.winfo_y()+25)
        elif self.direction == Direction.LEFT:
            self.place(x=self.winfo_x()-25)
        elif self.direction == Direction.RIGHT:
            self.place(x=self.winfo_x()+25)

        # apple detection

        for apple in self.master.winfo_children():
            if isinstance(apple, Apple) and self.winfo_x() == apple.winfo_x() and self.winfo_y() == apple.winfo_y():
                apple.place_forget()
                apple.destroy()

        self.master.after(self.speed, self.move)

