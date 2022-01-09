from turtle import *

ttl = Turtle()
w = ttl.getscreen()

def drawSpiral(t, lineLength):
    if lineLength > 0:
        t.forward(lineLength)
        t.right(90)
        drawSpiral(t, lineLength -5)
drawSpiral(ttl, 150)
w.exitonclick()

def tree(t, branchLength, branchDensity):
    if branchLength > 5:
        t.forward(branchLength)
        t.right(branchDensity)
        tree(t, branchLength - 15, branchDensity)
        t.left(branchDensity * 2)
        tree(t, branchLength -10, branchDensity)
        t.right(branchDensity)
        t.backward(branchLength)

tree(ttl, 100, 40)
w.exitonclick()
