import turtle
snoopy = turtle.Turtle()

def square():
  for x in range(0,4):
    snoopy.forward(90)
    snoopy.left(90)

def circle():
  for x in range(0,360):
    snoopy.forward(2)
    snoopy.left(1)

def triangle():
  for x in range(0,3):
    snoopy.forward(100)
    snoopy.left(120)

def parallelogram():
  for x in range(0,4):
    snoopy.forward(100)
    snoopy.left(45)
    snoopy.forward(100)
    snoopy.left(135)

def hexagon():
  for x in range(0,6):
    snoopy.forward(200)
    snoopy.left(60)
circle()
