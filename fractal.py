import turtle
import math

def draw_line(init_len):
 turtle.forward(init_len)
 turtle.left(45)
 turtle.forward(init_len)
 turtle.right(90)
 turtle.forward(init_len)
 turtle.left(45)
 turtle.forward(init_len)

def draw_fractal2(init_len):
  draw_line(init_len)
  turtle.left(45)
  draw_line(init_len)
  turtle.right(90)
  draw_line(init_len)
  turtle.left(45)
  draw_line(init_len)

def draw_fractal3(init_len):
  draw_fractal2(init_len)
  turtle.left(45)
  draw_fractal2(init_len)
  turtle.right(90)
  draw_fractal2(init_len)
  turtle.left(45)
  draw_fractal2(init_len)
  
  
def draw_fractal( big_len):
  if (big_len < 5):
    draw_line(big_len)
  else:
    small_len = big_len / (2 + math.sqrt(2))
    draw_fractal( small_len)
    turtle.left(45)
    draw_fractal( small_len)
    turtle.right(90)
    draw_fractal( small_len)
    turtle.left(45)
    draw_fractal(small_len)
  