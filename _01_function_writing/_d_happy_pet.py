"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    window = Tk()
    window.withdraw()
    pet = simpledialog.askstring("Prompt", "What pet (dog/cat/fish)")
    if pet == "dog" or pet == "cat" or pet == "fish":
        happiness = 0
        def feed():
            happiness += 1
            messagebox.showinfo("Message", "You fed your " + pet)
        def walk():
            if pet != "fish":
                happiness += 2
            else:
                happiness -= 100
            messagebox.showinfo("Message", "You walked your " + pet)
        def play():
            if pet != "cat":
                happiness += 2
            else:
                happiness += 1
            messagebox.showinfo("Message", "You played with your " + pet)
        while happiness < 100:
            interaction = simpledialog.askstring("Prompt", "What do you want to do with your pet (feed/walk/play)")
            if interaction == "feed":
                feed()
            elif interaction == "walk":
                walk()
            elif interaction == "play":
                play()
        messagebox.showinfo("Message", "Your pet is happy")
    else:
        messagebox.showerror("Error", "Invalid pet")
    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
    pass
