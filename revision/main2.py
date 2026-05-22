import turtle
pen=turtle.Turtle()
paper=turtle.Screen()
pen.speed(10)

pen.up()
pen.goto(250,-370)
pen.down()

for i in range(4):
    pen.forward(200)
    pen.left(90)

pen.up()
pen.goto(250,170)
pen.down()

for i in range(4):
    pen.forward(200)
    pen.left(90)

pen.up()
pen.goto(-440,170)
pen.down()

for i in range(4):
    pen.forward(200)
    pen.left(90)

pen.up()
pen.goto(-440,-370)
pen.down()

for i in range(4):
    pen.forward(200)
    pen.left(90)

pen.hideturtle()
turtle.done()
