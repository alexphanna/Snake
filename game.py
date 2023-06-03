from tkinter import *
from tkinter import ttk
from apple import Apple
from config import Config
from direction import Direction
from snake import Snake

root = Tk()
frame = Frame(root, background="black", width=Config.GRID_COLUMNS * Config.PIXEL_SIZE, height=Config.GRID_ROWS * Config.PIXEL_SIZE)
frame.pack()
frame.grid_propagate(FALSE)

for row in range(Config.GRID_COLUMNS):
    frame.rowconfigure(row, minsize=Config.PIXEL_SIZE, weight=1)
for column in range(Config.GRID_ROWS):
    frame.columnconfigure(column, minsize=Config.PIXEL_SIZE, weight=1)

snake = Snake(frame)
Apple(frame)

root.bind('<Key-w>', lambda e: snake.set_direction(Direction.UP))
root.bind('<Key-a>', lambda e: snake.set_direction(Direction.LEFT))
root.bind('<Key-s>', lambda e: snake.set_direction(Direction.DOWN))
root.bind('<Key-d>', lambda e: snake.set_direction(Direction.RIGHT))

frame.after(snake.speed, snake.move)
root.mainloop()
