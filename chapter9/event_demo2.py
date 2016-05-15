import tkinter as tk

class enlargrcirle(object):
	"""docstring for enlargrcirle"""
	def __init__(self):
		super(enlargrcirle, self).__init__()
		# self.arg = arg
		self.radius=50

		window=tk.Tk()
		window.title('control demo')

		self.canvas=tk.Canvas(window,bg='white',width=200,height=200)
		self.canvas.pack()
		self.canvas.create_oval(100-self.radius,100-self.radius,100+self.radius,100+self.radius,tags='oval')

		self.canvas.bind('<Button-1>',self.increase)
		self.canvas.bind('<Button-3>',self.decrease)

		window.mainloop()

	def increase(self,event):
		self.canvas.delete('oval')

		if self.radius<100:
			self.radius+=2
		self.canvas.create_oval(100-self.radius,100-self.radius,100+self.radius,100+self.radius,tags='oval')

	def decrease(self,event):
		self.canvas.delete('oval')

		if self.radius>2:
			self.radius-=2
		self.canvas.create_oval(100-self.radius,100-self.radius,100+self.radius,100+self.radius,tags='oval')

enlargrcirle()
