# This is practice using a turtle (little arrow that leaves a line like an Etch a Sketch) to draw things in Python
# Lets draw a square!
import turtle
t = turtle.Pen()

t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)

# Reset will return the turtle to the start and clear the drawing
t.reset()

# Clear will leave the turtle where he is but still clear the drawing
# t.clear()

# We can also turn the turtle right and backward. Similarly, we can tell the turtle to go UP, like lifting a pencil off of a page
# and DOWN to start drawing again

t.backward(100)
t.up()
t.right(90)
t.forward(20)
t.left(90)
t.down()
t.forward(100)

# More practice!

# Rectangle

t.reset()
t.forward(400)
t.left(90)
t.forward(200)
t.left(90)
t.forward(400)
t.left(90)
t.forward(200)
t.left(90)

# Triangle
t.reset()
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)

# Box without corners
t.reset()
t.up()
t.forward(100)
t.down()
t.forward(100)
t.up()
t.forward(100)
t.left(90)
t.forward(100)
t.down()
t.forward(100)
t.up()
t.forward(100)
t.left(90)
t.forward(100)
t.down()
t.forward(100)
t.up()
t.forward(100)
t.left(90)
t.forward(100)
t.down()
t.forward(100)
t.up()
t.forward(100)
t.left(90)


# This is just here to keep the window from closing. After it's done it generally just closes unless we ask for an input.
input("Press any key to exit ...")
