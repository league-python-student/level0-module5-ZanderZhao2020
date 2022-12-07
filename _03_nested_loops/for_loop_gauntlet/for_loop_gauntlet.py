"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""


if __name__ == '__main__':
    for c in range(101):
        print(c)
    for c in range(100, -1, -1):
        print(c)
    for c in range(2, 101, 2):
        print(c)
    for c in range(1, 100, 2):
        print(c)
    for c in range(1, 501):
        if c % 2 == 0:
            print(str(c) + " is even")
        else:
            print(str(c) + " is odd")
    for c in range(0, 778, 7):
        print(c)
    for c in range(2008, 2023):
        print("In " + str(c) + ", I was " + str(c - 2008) + " years old")
    for c in range(3):
        for d in range(3):
            print(str(c) + " " + str(d))
    for c in range(1, 8, 3):
        for d in range(c, c + 3):
            print(d, end=" ")
        print()
    for c in range(1, 101, 10):
        for d in range(c, c + 10):
            print(d, end=" ")
        print()
    for c in range(1, 7):
        for d in range(c):
            print("*", end=" ")
        print()
    pass
