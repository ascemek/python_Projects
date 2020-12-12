
from graphics import *
from random import *
from time import *
import random

#Create a window
win = GraphWin("My Program", 600,600)
win.setBackground("green")

key = win.checkKey()
circles = []

#Make 10 circles at different locations
for _ in range(10):
    rand_x = randint(20,580)
    rand_y = randint(20,580)
    rand_point = Point(rand_x, rand_y)

    my_circle = Circle(rand_point, 20)
    my_circle.setFill("red")
    my_circle.draw(win)
    circles.append(my_circle)

#Slow downs the circles so we can see
def delay(d):
    for i in range (d):
        for i in range (1500):
            pass

dx = random.randint(-1,3)
dy = random.randint(-1,3)

#Moves the circle and keep them inside the boundaries
while True:
    
    for my_circle in circles:
        my_circle.move(dx,dy)
        d = 100
        delay(d)

        p = my_circle.getCenter()
        if ((p.getX() - 20) <= 0.0) or ((p.getX() + 20) >= 600.0):
            dx = -dx
        if ((p.getY() - 20) <= 0.0) or ((p.getY() + 20) >= 600.0):
            dy = -dy


#Check for collisions between the circles
for i in range (0,len(circles)):
    for j in range (i+1), len(circles):
        #Check for a collision
        if circles[i].distance(circles[j]) < 20:
            temp_dx = circles[i].dx
            temp_dy = circles[i].dy

            circles[i].dx = circles[j].dx
            circles[i].dy = circles[j].dx

            circles[j].dx = temp_dx
            circles[j].dy = temp_dy

win.getMouse()
win.close
