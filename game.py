from tkinter import *
from tkinter import ttk
from snake import Snake
from apple import Apple
from direction import Direction

root = Tk()
frame = Frame(root, background="black", width=250, height=250)
frame.pack()

snake = Snake(frame)
Apple(frame)

root.bind('<Key-w>', lambda e: if snake.direction != Direction.DOWN: snake.set_direction(Direction.UP))
root.bind('<Key-a>', lambda e: snake.set_direction(Direction.LEFT))
root.bind('<Key-s>', lambda e: snake.set_direction(Direction.DOWN))
root.bind('<Key-d>', lambda e: snake.set_direction(Direction.RIGHT))

frame.after(snake.speed, snake.move)
root.mainloop()
