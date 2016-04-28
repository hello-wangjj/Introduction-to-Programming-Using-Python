import turtle
x1,y1=eval(input('enter the center of a circle x,y:'))
radius=eval(input('enter the radius of the circle:'))
x2,y2=eval(input('enter a point x,y:'))

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(x2,y2)
turtle.pendown()
turtle.begin_fill()
turtle.color('red')
turtle.circle(3)
turtle.end_fill()

turtle.penup()
turtle.goto(x1-70,y1-radius-20)
turtle.down()
d=((x2-x1)**2+(y2-y1)**2)**0.5

if d<=radius:
	turtle.write('The poin is inside the circle')
else:
	turtle.write('The poin is outside the circle')

turtle.hideturtle()
turtle.done()