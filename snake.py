from tkinter import *
from tkinter import ttk
from enum import Enum

class Snake(Frame):
    def __init__(self, parent):
        self.direction = Direction.DOWN
        self.speed = 500
        super().__init__(master=parent, background="lime", width=25, height=25)
        self.place(x=0, y=0)
    def set_direction(self, direction):
        self.direction = direction
    def move(self):
        if self.direction == Direction.UP:
            self.place(y=self.winfo_y()-25)
        elif self.direction == Direction.DOWN:
            self.place(y=self.winfo_y()+25)
        elif self.direction == Direction.LEFT:
            self.place(x=self.winfo_x()-25)
        elif self.direction == Direction.RIGHT:
            self.place(x=self.winfo_x()+25)
        root.after(snake.speed, snake.move)

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

root = Tk()
frame = Frame(root, background="black", width=250, height=250)
frame.pack()

snake = Snake(frame)

root.bind('<Key-w>', lambda e: snake.set_direction(Direction.UP))
root.bind('<Key-a>', lambda e: snake.set_direction(Direction.LEFT))
root.bind('<Key-s>', lambda e: snake.set_direction(Direction.DOWN))
root.bind('<Key-d>', lambda e: snake.set_direction(Direction.RIGHT))

root.after(snake.speed, snake.move)
root.mainloop()
