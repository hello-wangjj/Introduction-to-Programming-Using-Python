import tkinter as tk
import random

class BounceBalls(object):
	"""docstring for BounceBalls"""
	def __init__(self):
		super(BounceBalls, self).__init__()
		# self.arg = arg
		self.ballList=[]
		window=tk.Tk()
		window.title('Bouncing Balls')

		self.width=350
		self.height=150
		self.canvas=tk.Canvas(window,bg='white',
					width=self.width,height=self.height)
		self.canvas.pack()


		frame=tk.Frame(window)
		frame.pack()
		btStop=tk.Button(frame,text='stop',command=self.stop)
		btStop.pack(side=tk.LEFT)
		btResume=tk.Button(frame,text='resume',command=self.resume)
		btResume.pack(side=tk.LEFT)
		btAdd=tk.Button(frame,text='+',command=self.add)
		btAdd.pack(side=tk.LEFT)
		btRemove=tk.Button(frame,text='-',command=self.remove)
		btRemove.pack(side=tk.LEFT)

		self.sleeptime=100
		self.isStop=False
		self.animate()
		window.mainloop()



	def stop(self):
		# pass
		self.isStop=True

	def resume(self):
		# pass
		self.isStop=False
		self.animate()

	def add(self):
		# pass
		self.ballList.append(Ball())

	def remove(self):
		# pass
		self.ballList.pop()

	def animate(self):
		# pass
		while not self.isStop:
			# pass
			self.canvas.after(self.sleeptime)
			self.canvas.update()
			self.canvas.delete('ball')

			for  ball in self.ballList:
				self.redisplayBall(ball)

	def redisplayBall(self,ball):
		# pass
		if ball.x>self.width or ball.x<0:
			ball.dx=-ball.dx
		if ball.y>self.height or ball.y<0:
			ball.dy=-ball.dy

		ball.x+=ball.dx
		ball.y+=ball.dy
		self.canvas.create_oval(ball.x-ball.radius,ball.y-ball.radius,ball.x+ball.radius,ball.y+ball.radius,fill=ball.color,tags='ball')

class Ball(object):
	"""docstring for Ball"""
	def __init__(self):
		super(Ball).__init__()
		# self.arg = arg
		self.x=0
		self.y=0
		self.dx=2
		self.dy=2
		self.radius=3
		self.color=getRandomColor()

def getRandomColor():
	color='#'
	for j in range(6):
		color+=toHexChar(random.randint(0,15))
	return color

def toHexChar(hexValue):
	if 0<hexValue<=9:
		return chr(hexValue+ord('0'))
	else:
		return chr(hexValue-10+ord('A'))


BounceBalls()