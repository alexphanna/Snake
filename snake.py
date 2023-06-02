from tkinter import *
from apple import Apple
from direction import Direction

class Snake(list):
    def __init__(self, master):
        self.direction = Direction.DOWN
        self.speed = 500
        self.master = master
        front = Frame(master=self.master, background="lime", width=25, height=25)
        front.place(x = 0, y = 0)
        self.append(front)
        self.grow()
    def grow(self):
        frame = Frame(master=self.master, background="lime", width=25, height=25)
        if self.direction == Direction.UP:
            frame.place(x = self[len(self) - 1].winfo_x(), y = self[len(self) - 1].winfo_y() + 25)
        elif self.direction == Direction.DOWN:
            frame.place(x = self[len(self) - 1].winfo_x(), y = self[len(self) - 1].winfo_y() - 25)
        elif self.direction == Direction.LEFT:
            frame.place(x = self[len(self) - 1].winfo_x() + 25, y = self[len(self) - 1].winfo_y())
        elif self.direction == Direction.RIGHT:
            frame.place(x = self[len(self) - 1].winfo_x() - 25, y = self[len(self) - 1].winfo_y())
        self.append(frame)
    def set_direction(self, direction):
        self.direction = direction
    def move(self):
        # moves the snake in the current direction

        if self.direction == Direction.UP:
            self[0].place(y = self[0].winfo_y() - 25)
        elif self.direction == Direction.DOWN:
            self[0].place(y = self[0].winfo_y() + 25)
        elif self.direction == Direction.RIGHT:
            self[0].place(x = self[0].winfo_x() + 25)
        elif self.direction == Direction.LEFT:
            self[0].place(x = self[0].winfo_x() - 25)
        

        n = len(self) - 1
        while n > 0:
            self[n].place(x = self[n - 1].winfo_x(), y = self[n - 1].winfo_y())
            n -= 1

        # apple detection

        for apple in self.master.winfo_children():
            if isinstance(apple, Apple) and self[0].winfo_x() == apple.winfo_x() and self[0].winfo_y() == apple.winfo_y():
                apple.place_forget()
                apple.destroy()
                self.grow()
                Apple(frame)

        self.master.after(self.speed, self.move)

