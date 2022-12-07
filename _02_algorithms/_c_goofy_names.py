"""
Write an algorithm to change a string into a "goofy" version.
"""
import random
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    # TODO)
    #  1. Ask the user to enter their name.
    window = Tk()
    window.withdraw()
    name = simpledialog.askstring("Prompt", "What is your name?")
    #  2. Use a loop to alternately modify each character of the name into
    #     uppercase and lowercase letters until a new "goofy" representation
    #     of their name has been constructed.
    #     For example, if they enter their name as Alexander Hamilton
    #     their goofy name will be AlExAnDeR HaMiLtOn
    goofy = ""
    for char in name:
        if random.randint(1, 2) == 1:
            goofy += char.upper()
        else:
            goofy += char.lower()
    #  3. Show the user the goofy version of their name in a pop-up.
    messagebox.showinfo("Message", "The goofy version of your name is " + goofy)
    pass
