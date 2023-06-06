from tkinter import *
from apple import Apple
from config import config
from direction import Direction

class Snake(list):
    def __init__(self, master):
        self.alive = True
        self.direction = Direction.RIGHT
        self.speed = 100         
        self.moved = False
        self.master = master
        front = Frame(master=self.master, background="lime", width=config["pixel_size"], height=config["pixel_size"], name="front")
        front.grid(row=1, column=1)
        self.append(front)
    def grow(self):
        self.append(Frame(master=self.master, background="lime", width=config["pixel_size"], height=config["pixel_size"]))
    def kill(self):
        self.alive = False
    def set_direction(self, direction):
        if -direction.value != self.direction.value and direction.value != self.direction.value:
            if self.moved is False:
                self.move()
            self.direction = direction
            self.moved = False
    def move(self):
        if self.direction == Direction.UP or self.direction == Direction.DOWN:
            row = self[0].grid_info()['row'] + (int)(self.direction.value / abs(self.direction.value))
            if row == config["grid_rows"]:
                if config["god_mode"]:
                    self[0].grid(row = 0)
                else:
                    self.kill()
            elif row == -1:
                if config["god_mode"]:
                    self[0].grid(row = config["grid_rows"] - 1)
                else:
                    self.kill()
            else:
                self[0].grid(row = row)
        elif self.direction == Direction.RIGHT or self.direction == Direction.LEFT:
            column = self[0].grid_info()['column'] + (int)(self.direction.value / abs(self.direction.value))
            if column == config["grid_columns"]:
                if config["god_mode"]:
                    self[0].grid(column = 0)
                else:
                    self.kill()
            elif column == -1:
                if config["god_mode"]:
                    self[0].grid(column = config["grid_columns"] - 1)
                else:
                    self.kill()
            else:
                self[0].grid(column = column)
        for frame in self.master.winfo_children():
            if frame.grid_info() == self[0].grid_info():
                if isinstance(frame, Apple):
                    frame.grid_remove()
                    self.grow()
                    Apple(self.master)
                elif config["god_mode"] == False and frame.winfo_name() != "front":
                    self.kill()

        index = len(self) - 1
        while index > 0:
            self[index].grid(row = self[index - 1].grid_info()['row'], column = self[index - 1].grid_info()['column'])
            index -= 1

        self.moved = True
    def start(self):
        if self.alive:
            self.move()
            self.master.after(self.speed, self.start)
