"""
Have the turtle draw a row of houses.
"""
import random
import turtle
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    # TODO)
    #   1) Move the turtle to the left side of the window near the bottom.
    bob = turtle.Turtle()
    bob.penup()
    bob.setx(-470)
    bob.pendown()
    #   2) Draw ONE flat-topped house with height=100 and green grass after it.
    def draw_house(height):
        bob.color("green")
        bob.forward(20)
        bob.color("black")
        for c in range(4):
            if c % 2 == 0:
                bob.forward(40)
            else:
                bob.forward(height)
            bob.left(90)
        bob.forward(40)
        bob.color("green")
        bob.forward(20)
    #   3) Put the code that drew the house into a function called draw_house
    #      HINT: Only the code that draws one house should go in this function.
    #   4) Using the function you just created, draw 10 houses.
    #      HINT: Use a for loop.
    for c in range(10):
        draw_house(random.randint(40, 200))
    #   5) Run the code to make sure it works before proceeding.
    #   6) Now change the draw_house function to take height as a parameter.
    #   7) Use random numbers to draw 9 houses of different heights.
    #   8) Run the code to make sure it works before proceeding.
    #   9) Make the draw_house function's height input a string and set the
    #      height of the house based on the following:
    #         “small”            =  60
    #         “medium”           =  120
    #         “large”            =  250

    #   10) Make two new functions that draw different shaped roofs
    #      (JUST the roof part): draw_pointy_roof, draw_flat_roof
    #   11) By calling the correct "roof" function, make large houses have
    #      flat roofs and all the others have pointy roofs.
    turtle.done()
    pass
