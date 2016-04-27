import turtle

x1,y1=eval(input('enter the point1:'))
x2,y2=eval(input('enter the point2:'))

p1='('+str(x1)+str(y1)+')'
p2='('+str(x2)+str(y2)+')'


turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write(p1)
turtle.goto(x2,y2)
turtle.write(p2)

turtle.hideturtle()
turtle.done()