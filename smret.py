#from c1 import graphics
from c1graphic import *


def main():
    win = GraphWin('Face', 200, 150) # give title and dimensions
    win.yUp() # make right side up coordinates!

    head = Circle(Point(40,100), 25) # set center and radius
    head.setFill("yellow")
    head.draw(win)

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = Oval(Point(30, 90), Point(50, 85)) # set corners of bounding box
    mouth.setFill("red")
    mouth.draw(win)

    label = Text(Point(100, 120), 'A face')
    label.draw(win)

    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()

main()


 draw color filled circle in turtle
  
import turtle
  
# creating turtle pen
t = turtle.Turtle()
  
# taking input for the radius of the circle
r = int(input("Enter the radius of the circle: "))
  
# taking the input for the color
col = input("Enter the color name or hex value of color(# RRGGBB): ")
  
# set the fillcolor
t.fillcolor(col)
  
# start the filling color
t.begin_fill()
  
# drawing the circle of radius r
t.circle(r)
  
# ending the filling of the color
t.end_fill()