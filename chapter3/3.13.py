import turtle
turtle.pensize(3)
turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.setheading(30)
turtle.begin_fill()
turtle.color('red')
turtle.circle(80,steps=6)
turtle.end_fill()

turtle.penup()
turtle.goto(-80,0)
turtle.pendown()
turtle.color('white')
turtle.write('STOP',font=('Times',20,'bold'))

turtle.hideturtle()
turtle.done()