"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle


if __name__ == '__main__':
    # TODO)
    #   1. Create a turtle.
    bob = turtle.Turtle()
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.
    def square():
        bob.circle(100, 360, 4)
    def triangle():
        bob.circle(100, 360, 3)
    def circle():
        bob.circle(100, 360, 360)
    #   3. Ask the user for the for a shape to draw.
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    shape = simpledialog.askstring("Prompt", "What shape (square/triangle/circle)")
    if shape == "square":
        square()
    elif shape == "triangle":
        triangle()
    elif shape == "circle":
        circle()
    else:
        messagebox.showerror("Error", "Invalid shape")
    pass
