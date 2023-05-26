from tkinter import *
from snake import Snake

def handle_keypressed(event):
    if event.char == "w": snake.moveUp()
    elif event.char == "a": snake.moveLeft()
    elif event.char == "s": snake.moveDown()
    elif event.char == "d": snake.moveRight()

window = Tk()

frame = Frame(
    master=window,
    width=256,
    height=256,
    bg="black"
).pack()
snake = Snake(frame)

window.bind("<Key>", handle_keypressed)
window.mainloop()