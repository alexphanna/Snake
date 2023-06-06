from tkinter import *
from apple import Apple
from config import config
from direction import Direction
from snake import Snake

root = Tk()
frame = Frame(root, background="black", width=config["grid_columns"] * config["pixel_size"], height=config["grid_rows"] * config["pixel_size"])
frame.pack()
frame.grid_propagate(FALSE)

for row in range(config["grid_columns"]):
    frame.rowconfigure(row, minsize=config["pixel_size"], weight=1)
for column in range(config["grid_rows"]):
    frame.columnconfigure(column, minsize=config["pixel_size"], weight=1)

snake = Snake(frame)
Apple(frame)

root.bind('<Key-w>', lambda e: snake.set_direction(Direction.UP))
root.bind('<Key-a>', lambda e: snake.set_direction(Direction.LEFT))
root.bind('<Key-s>', lambda e: snake.set_direction(Direction.DOWN))
root.bind('<Key-d>', lambda e: snake.set_direction(Direction.RIGHT))

snake.start()
root.mainloop()
 