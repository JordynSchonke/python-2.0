import turtle
pen=turtle.Turtle()
paper=turtle.Screen()

pen.color("purple")

pen.fillcolor("red")
pen.begin_fill()

for i in range(3):
    pen.forward(200)
    pen.left(120)
pen.end_fill()

pen.up()
pen.goto(0,120)
pen.down()

pen.begin_fill()
for i in range(3):
    pen.forward(200)
    pen.right(120)
pen.end_fill()

turtle.done()