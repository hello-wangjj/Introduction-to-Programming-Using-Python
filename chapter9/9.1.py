import tkinter as tk

class MoveCircle(object):
	"""docstring for MoveCircle"""
	def __init__(self):
		super(MoveCircle, self).__init__()
		# self.arg = arg
		window=tk.Tk()
		window.title('move circle')

		self.x=2
		self.radius=10

		frame1=tk.Frame(window)
		frame1.pack()
		self.canvas=tk.Canvas(frame1,bg='white',width=400,height=400)
		self.canvas.pack()
		self.canvas.create_oval(self.radius,self.radius,self.radius+10,self.radius+10,fill='red',tags='oval')


		frame2=tk.Frame(window)
		frame2.pack()

		btnLeft=tk.Button(frame2,text='left',command=self.MoveLeft)
		btnRight=tk.Button(frame2,text='right',command=self.MoveRight)
		btnUp=tk.Button(frame2,text='up',command=self.MoveUp)
		btnDown=tk.Button(frame2,text='down',command=self.MoveDown)
		btnLeft.grid(row=1,column=1,sticky=tk.W)
		btnRight.grid(row=1,column=2)
		btnUp.grid(row=1,column=3)
		btnDown.grid(row=1,column=4)

		window.mainloop()



	def MoveLeft(self):
		# pass
		self.canvas.delete('oval')
		if self.radius>0:
			self.radius-=2
			self.canvas.create_oval(self.radius,10,self.radius+10,20,fill='red',tags='oval')
		else:
			self.canvas.create_oval(0,10,10,20,fill='red',tags='oval')

	def MoveRight(self):
		# pass
		self.canvas.delete('oval')
		if self.radius<400:
			self.radius+=2
			self.canvas.create_oval(self.radius,10,self.radius+10,20,fill='red',tags='oval')
		else:
			self.canvas.create_oval(380,10,400,20,fill='red',tags='oval')
	def MoveUp(self):
		pass
	def MoveDown(self):
		pass


MoveCircle()


