from tkinter import *
from apple import Apple
from config import Config
from direction import Direction

class Snake(list):
    def __init__(self, master):
        self.direction = Direction.DOWN
        self.speed = 100
        self.master = master
        front = Frame(master=self.master, background="lime", width=Config.PIXEL_SIZE, height=Config.PIXEL_SIZE)
        front.grid(row=0, column=0)
        self.append(front)
        self.grow()
    def grow(self):
        self.append(Frame(master=self.master, background="lime", width=Config.PIXEL_SIZE, height=Config.PIXEL_SIZE))
    def set_direction(self, direction):
        if -direction.value != self.direction.value:
            self.direction = direction
    def move(self):
        if self.direction == Direction.UP or self.direction == Direction.DOWN:
            self[0].grid(row = self[0].grid_info()['row'] + (int)(self.direction.value / abs(self.direction.value)))
        elif self.direction == Direction.RIGHT or self.direction == Direction.LEFT:
            self[0].grid(column = self[0].grid_info()['column'] + (int)(self.direction.value / abs(self.direction.value)))

        index = len(self) - 1
        while index > 0:
            self[index].grid(row = self[index - 1].grid_info()['row'], column = self[index - 1].grid_info()['column'])
            index -= 1

        for apple in self.master.winfo_children():
            if isinstance(apple, Apple):
                for snake in self:
                    if snake.grid_info() == apple.grid_info():
                        apple.place_forget()
                        apple.grid_remove()
                        self.grow()
                        Apple(self.master)
                        break

        self.master.after(self.speed, self.move)
