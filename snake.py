from tkinter import *
from apple import Apple
from config import Config
from direction import Direction

class Snake(list):
    def __init__(self, master):
        self.direction = Direction.DOWN
        self.speed = 100         
        self.moved = False
        self.alive = True
        self.master = master
        front = Frame(master=self.master, background="lime", width=Config.PIXEL_SIZE, height=Config.PIXEL_SIZE, name="front")
        front.grid(row=1, column=1)
        self.append(front)
        self.grow()
    def grow(self):
        self.append(Frame(master=self.master, background="lime", width=Config.PIXEL_SIZE, height=Config.PIXEL_SIZE))
    def set_direction(self, direction):
        if -direction.value != self.direction.value and direction.value != self.direction.value:
            if self.moved is False:
                self.move()
            self.direction = direction
            self.moved = False
    def move(self):
        if self.direction == Direction.UP or self.direction == Direction.DOWN:
            row = self[0].grid_info()['row'] + (int)(self.direction.value / abs(self.direction.value))
            if row == Config.GRID_ROWS:
                self[0].grid(row = 0)
            elif row == -1:
                self[0].grid(row = Config.GRID_ROWS - 1)
            else:
                self[0].grid(row = row)
        elif self.direction == Direction.RIGHT or self.direction == Direction.LEFT:
            column = self[0].grid_info()['column'] + (int)(self.direction.value / abs(self.direction.value))
            if column == Config.GRID_COLUMNS:
                self[0].grid(column = 0)
            elif column == -1:
                self[0].grid(column = Config.GRID_COLUMNS - 1)
            else:
                self[0].grid(column = column)
        for frame in self.master.winfo_children():
            if frame.grid_info() == self[0].grid_info():
                if isinstance(frame, Apple):
                    frame.grid_remove()
                    self.grow()
                    Apple(self.master)
                elif frame.winfo_name() != "front":
                    self.alive = False

        index = len(self) - 1
        while index > 0:
            self[index].grid(row = self[index - 1].grid_info()['row'], column = self[index - 1].grid_info()['column'])
            index -= 1

        self.moved = True
    def start(self):
        if self.alive:
            self.move()
            self.master.after(self.speed, self.start)
