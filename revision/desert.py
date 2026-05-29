import turtle
pen=turtle.Turtle()
paper=turtle.Screen()
pen.speed(100)

#pyramid

pen.fillcolor('orange')
pen.begin_fill()

pen.up()
pen.goto(-400,0)
pen.down()

for i in range(3):
    pen.forward(300)
    pen.left(120)

pen.end_fill()

#sun

pen.fillcolor('yellow')
pen.begin_fill()

pen.up()
pen.goto(250,200)
pen.down()

for i in range(4):
    pen.forward(150)
    pen.left(90)

pen.end_fill()

pen.right(45)

pen.fillcolor('yellow')
pen.begin_fill()

pen.up()
pen.goto(230,270)
pen.down()

for i in range(4):
    pen.forward(150)
    pen.left(90)

pen.end_fill()

#half cirle
pen.left(45)

pen.up()
pen.goto(100,0)
pen.down()
pen.left(90)

pen.fillcolor('red')
pen.begin_fill()

for i in range(19):
    pen.forward(15)
    pen.right(10)

pen.end_fill()

pen.up()
pen.goto(-500,0)
pen.down()
pen.left(100)

pen.color("blue")

pen.forward(990)

#cactus

pen.up()
pen.goto(150,90)
pen.down()
pen.left(90)

pen.forward(60)
pen.right(90)
pen.circle(60,60)
pen.left(90)
pen.circle()

turtle.done()