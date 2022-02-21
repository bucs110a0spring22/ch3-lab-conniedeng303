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
# leonardo.speed(1)
# michelangelo.speed(1)
## 5. your code goes here

x = random.randrange(1,101)
c = random.randrange(1,101)
leonardo.forward(x)
michelangelo.forward(c)
leonardo.goto(-100,-20)
michelangelo.goto(-100,20)

for i in (1,11):
  x = random.randrange(1,101)
  c = random.randrange(1,101)
  leonardo.forward(x)
  michelangelo.forward(c)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part B - complete part B here
# for counter in range(list(3,4,6,6,9,12)

sides = [3,4,6,9,12]
for item in sides:
  leonardo.clear()
  leonardo.goto(0,0)
  for n in range(item):
      leonardo.down()
      leonardo.pensize(3)
      leonardo.forward(50)
      leonardo.right(360/item)
      
sides = [3,4,6,9,12]
for item in sides:
  leonardo.clear()
  leonardo.goto(0,0)
  for n in range(item):
      leonardo.down()
      leonardo.pensize(3)
      leonardo.forward(50)
      leonardo.right(360/item)

# def turtle_draw (degree=None):
#   leonardo.clear()
#   leonardo.goto(0,0)
#   for n in range(degree):
#       leonardo.down()
#       leonardo.pensize(3)
#       leonardo.forward(50)
#       leonardo.right(360/degree)

# turtle_draw(degree=3)
# turtle_draw(degree=4)
# turtle_draw(degree=6)
# turtle_draw(degree=9)
# turtle_draw(degree=12)

window.exitonclick()



