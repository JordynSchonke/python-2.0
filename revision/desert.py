import turtle
pen=turtle.Turtle()
paper=turtle.Screen()
pen.speed(100)
paper.bgcolor("#0D4ABD")

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
pen.fillcolor("#C7AE20")
pen.begin_fill()

for i in range(2):
    pen.forward(1000)
    pen.right(90)
    pen.forward(400)
    pen.right(90)

pen.end_fill()

#cactus

pen.up()
pen.goto(200,90)
pen.down()
pen.left(90)

pen.fillcolor('green')
pen.begin_fill()

pen.forward(60)
pen.right(90)
pen.circle(60,60)
pen.circle(20,60)
pen.circle(20,40)
pen.circle(60,60)
pen.circle(0,60)
pen.right(180)
pen.circle(60,60)
pen.circle(20,40)
pen.circle(20,30)
pen.circle(60,60)
pen.circle(20,0)
pen.circle(30,0)
pen.right(80)
pen.circle(60,60)
pen.circle(20,30)
pen.circle(20,5)
pen.circle(20,60)
pen.forward(10)
pen.right(60)
pen.forward(40)

pen.end_fill()
turtle.done()