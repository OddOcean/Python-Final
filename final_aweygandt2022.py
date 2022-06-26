from tkinter import *
import time

# Create dimensions for inner box and rectangle
WIDTH = 600
HEIGHT = 500
SIZE = 50
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()
color = 'red'
canvas.create_rectangle(250, 200, 350, 300, tags="rect", fill="black")

# Create a class for the ball with its coordinates to start from, the size, color, speed  and allowing the ball to move
class Ball:
  def __init__(self):
    self.shape = canvas.create_oval(550, 1, 550 + SIZE, SIZE, fill=color)
    self.speedx = -8  # changed from 3 to 7
    self.speedy = 10  # changed from 3 to 10
    self.active = True
    self.move_active()

  # Create def to update ball and its positioning allowing it to move back and fourth inside the box
  def ball_update(self):
    canvas.move(self.shape, self.speedx, self.speedy)
    pos = canvas.coords(self.shape)
    #for i in range(len(pos)):
      #print(i, pos[i])
    if pos[2] >= WIDTH or pos[0] <= 0:
      self.speedx *= -1
    if pos[3] >= HEIGHT or pos[1] <= 0:
      self.speedy *= -1

    # Top of the square #Give outline for inner black box top side of the balls boundaries
    if (pos[0] < 350 and pos[2] >= 250 and pos[3] >= 200 and pos[1] < 200 and self.speedy > 1 ):
      self.speedy *= -1
      print("top")
    #bottom of square. gives outline for just inside the bottom of the black box
    elif (pos[0] < 350 and pos[2] >= 250 and pos[3] > 300 and pos[1] <= 300 and self.speedy < 1):
      self.speedy *= -1
      print("bottom")
    #left of square. gives outline for just inside the left side of the black box
    elif (pos[0] < 250 and pos[2] >= 250 and pos[3] >= 200 and pos[1] < 300 and self.speedx > 1):
      self.speedx *= -1
      print("left")
    #right of square. gives outline for just inside the right side of the black box
    elif (pos[0] <= 350 and pos[2] > 350 and pos[3] >= 200 and pos[1] <= 300 and self.speedx < 1):
      self.speedx *= -1
      print("right")

  def move_active(self):
    if self.active:
      self.ball_update()
      tk.after(40, self.move_active)  # changed from 10ms to 30ms


ball = Ball()
tk.mainloop()
