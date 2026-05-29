import turtle
pen=turtle.Turtle()
paper=turtle.Screen()
pen.speed(10)

pen.color("purple")

pen.fillcolor("brown")
pen.begin_fill()

for i in range(4):
    pen.forward(200)
    pen.left(90) 

pen.end_fill()

pen.up()
pen.goto(0,200)
pen.down()

pen.fillcolor("green")
pen.begin_fill()

for i in range(3):
    pen.forward(200)
    pen.left(120)
pen.end_fill()

pen.up()
pen.goto(20,100)
pen.down()

pen.fillcolor("red")
pen.begin_fill()

for i in range(4):
    pen.forward(50)
    pen.left(90)
pen.end_fill()

pen.up()
pen.goto(130,100)
pen.down()

pen.fillcolor("red")
pen.begin_fill()

for i in range(4):
    pen.forward(50)
    pen.left(90)
pen.end_fill()

pen.up()
pen.goto(80,10)
pen.down()

pen.fillcolor("blue")
pen.begin_fill()

for i in range(4):
    pen.forward(50)
    pen.left(90)
pen.end_fill()

turtle.hideturtle()   
turtle.done()
