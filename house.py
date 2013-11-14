'''
Created on Sep 26, 2013

@author: pom
'''
import turtle

a = 1

def draw_house(curb_length, wall_height, roof_length):
 
  turtle.forward(curb_length)
  turtle.left(90)
  turtle.forward(wall_height)
  turtle.right(45)
  turtle.forward(roof_length)
  turtle.right(45)
  turtle.right(45)
  turtle.forward(roof_length)
  turtle.right(45)
  turtle.forward(wall_height)
  turtle.left(90)
  turtle.forward(curb_length)

def draw_street():
  turtle.clearscreen()
  draw_house(curb_length=10, wall_height=90, roof_length=70)
  draw_house(curb_length=10, wall_height=80, roof_length=60)
  draw_house(curb_length=20, wall_height=90, roof_length=80)
  