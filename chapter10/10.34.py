import turtle
import random

def getLowerCaseLetter():
	n=random.randint(97, 122)
	return chr(n)

# print (getLowerCaseLetter())

def drawHistogram(ls):
	WIDTH=600
	HEIGHT=300

	turtle.penup()
	turtle.goto(-WIDTH/2,-HEIGHT/2)
	turtle.pendown()
	turtle.forward(WIDTH)

	widthOfBar=WIDTH/(len(ls))

	for i in range(len(ls)):
		height=ls[i]*HEIGHT/max(ls)
		drawBar(-WIDTH/2+i*widthOfBar+10, -HEIGHT/2, widthOfBar-5, height)
		drawString(-WIDTH/2+i*widthOfBar+18, -HEIGHT/2-15, chr(i+ord('a')))
	turtle.hideturtle()


def drawBar(i,j,widthOfBar,height):
	turtle.penup()
	turtle.goto(i,j)
	turtle.setheading(90)
	turtle.pendown()

	turtle.forward(height)
	turtle.right(90)
	turtle.forward(widthOfBar)
	turtle.right(90)
	turtle.forward(height)

def drawString(i,j,ch):
	turtle.penup()
	turtle.goto(i,j)
	turtle.setheading(90)
	turtle.pendown()
	turtle.write(ch)

count=26*[0]
for i in range(1000):
	c=getLowerCaseLetter()
	count[ord(c)-ord('a')]+=1
drawHistogram(count)

turtle.done()