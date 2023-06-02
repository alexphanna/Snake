from tkinter import *
from tkinter import ttk
from snake import Snake
from apple import Apple
from direction import Direction

GRID_WIDTH = 25
GRID_HEIGHT = 25
PIXEL_SIZE = 25

root = Tk()
frame = Frame(root, background="black", width=GRID_WIDTH * PIXEL_SIZE, height=GRID_HEIGHT * PIXEL_SIZE)
frame.pack()
frame.grid_propagate(FALSE)

for row in range(GRID_WIDTH):
    frame.rowconfigure(row, minsize=PIXEL_SIZE, weight=1)
for column in range(GRID_HEIGHT):
    frame.columnconfigure(column, minsize=PIXEL_SIZE, weight=1)

snake = Snake(frame)
Apple(frame)

root.bind('<Key-w>', lambda e: snake.set_direction(Direction.UP))
root.bind('<Key-a>', lambda e: snake.set_direction(Direction.LEFT))
root.bind('<Key-s>', lambda e: snake.set_direction(Direction.DOWN))
root.bind('<Key-d>', lambda e: snake.set_direction(Direction.RIGHT))

frame.after(snake.speed, snake.move)
root.mainloop()
