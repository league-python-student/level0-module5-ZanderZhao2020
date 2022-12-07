r = 0.1;
plus = False
minus = False
def setup():
    size(800,500)
    smooth(8)
def draw():
    background(200)
    for i in range(300, 0, -10):
        pushMatrix();
        translate(width/4,height/4)
        noFill()
        strokeWeight(2)
        ellipse(r,100,i,i)
        popMatrix();
    for j in range(300, 0, -10):
        pushMatrix()
        translate(width/4,height / 4)
        noFill()
        ellipse(350 - r, 100, j, j)
        popMatrix()
    if r < 5:
        plus = True
        minus = False
    if r > 450:
        plus = False
        minus = True
    if plus:
        r = r + 0.2
    if minus:
        r = r - 0.1
