import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here

x = random.randrange(1,100)
c = random.randrange(1,100)
leonardo.forward(x)
michelangelo.forward(c)
leonardo.goto(-100,-20)
michelangelo.goto(-100,20)

for i in (1,11):
  x = random.randrange(1,100)
  c = random.randrange(1,100)
  leonardo.forward(x)
  michelangelo.forward(c)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part B - complete part B here

degree1: int(degree)

def turtle_draw (degree=None):
  leonardo.goto(0,0)
  for n in range(degree):
    leonardo.down()
    leonardo.pensize(3)
    leonardo.forward(50)
    leonardo.right(360/degree)
    
turtle_draw(degree=6)




window.exitonclick()
